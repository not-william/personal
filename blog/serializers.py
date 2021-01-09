from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Image, Post, Thing


class UserSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())

    class Meta:
        model = User
        fields = ["url", "username", "email", "groups", "images"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ["name"]


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    things = serializers.StringRelatedField(many=True)
    post = serializers.StringRelatedField()

    class Meta:
        model = Image
        fields = [
            "id",
            "description",
            "location",
            "snap_date",
            "order",
            "file",
            "lg_file",
            "sm_file",
            "f_number",
            "shutter_speed",
            "focal_length",
            "things",
            "post",
            "owner",
        ]


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    images = serializers.SerializerMethodField()

    def get_images(self, instance):
        images = instance.images.order_by("order")
        return ImageSerializer(images, many=True, context=self.context).data

    class Meta:
        model = Post
        fields = ["id", "text", "owner", "images"]
