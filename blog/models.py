from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image as PImage
from PIL.ExifTags import TAGS
from datetime import datetime
import numpy as np

class Post(models.Model):
    text = models.CharField(max_length=1000)
    order = models.IntegerField(null=True)

    class Meta:
        ordering = ('-order',)

    def __str__(self):
        return self.text


class Image(models.Model):
    description = models.CharField(max_length=240)
    location = models.CharField(max_length=150)
    snap_date = models.DateTimeField('date taken', editable=False, null=True)
    f_number = models.FloatField(editable=False, null=True)
    ISO = models.IntegerField(editable=False, null=True)
    focal_length = models.IntegerField(editable=False, null=True)
    shutter_speed = models.IntegerField(editable=False, null=True)
    owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images')
    post = models.ForeignKey('Post', related_name='images', on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        unique_together = ('post_id', 'order',)

    def save(self, *args, **kwargs):
        if self.file:
            image = PImage.open(self.file)
            exifdata = image.getexif()
            readable_data = {}
            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes 
                if isinstance(data, bytes):
                    data = data.decode()
                readable_data[tag] = data
            print(readable_data)
            f_number = readable_data["FNumber"]
            focal_length = readable_data["FocalLength"]
            ISO = readable_data["ISOSpeedRatings"]
            date_time_original = readable_data["DateTimeOriginal"]
            print(date_time_original)
            date_time_original = datetime.strptime(date_time_original, "%Y:%m:%d %H:%M:%S")
            shutter_speed = round(2**float(readable_data["ShutterSpeedValue"]))

            self.snap_date = date_time_original
            self.f_number = f_number
            self.ISO = ISO
            self.focal_length = focal_length
            self.shutter_speed = shutter_speed

            super(Image, self).save(*args, **kwargs)

            np_image = np.asarray(image)
            outputs = settings.PREDICTOR(np_image)
            outputs = outputs["instances"].to("cpu")
            objects = np.array(outputs.pred_classes)
            object_classes = settings.COCO_THINGS[objects]
            bboxes = outputs.pred_boxes

            for object_name, bbox in zip(object_classes, bboxes):
                object_row = Thing(
                    name=object_name,
                    image_id=self,
                    x_min=bbox[0],
                    y_min=bbox[1],
                    x_max=bbox[2],
                    y_max=bbox[3],
                )
                object_row.save()

            width, height = image.size

            factor = min(1080 / height, 1)
            size = int(width * factor), int(height * factor)
            image_lg = image.resize(size, PImage.ANTIALIAS)
            image_lg.save(self.file.path + ":lg", "JPEG", quality=95)

            factor = max(326 * 2 / height, 488 * 2 / width)
            size = int(width * factor), int(height * factor)
            image_sm = image.resize(size, PImage.ANTIALIAS)
            image_sm.save(self.file.path + ":sm", "JPEG", quality=95)

class Thing(models.Model):
    image_id = models.ForeignKey('Image', related_name="things", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    x_min = models.FloatField()
    x_max = models.FloatField()
    y_min = models.FloatField()
    y_max = models.FloatField()

    def __str__(self):
        return self.name