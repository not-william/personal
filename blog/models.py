from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    description = models.CharField(max_length=240)
    location = models.CharField(max_length=150)
    snap_date = models.DateTimeField('date taken')
    owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE)