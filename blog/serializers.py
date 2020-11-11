from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Image

class UserSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'images']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Image
        fields = ['id', 'description', 'location', 'snap_date', 'owner']