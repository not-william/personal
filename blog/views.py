from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from blog.serializers import UserSerializer, GroupSerializer, ImageSerializer
from blog.models import Image
from blog.permissions import IsOwnerOrReadOnly

def index(request):
    return HttpResponse("This is my blog.")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=None):
        if request.user and pk == 'me':
            return Response(self.serializer_class(request.user, context={'request': request}).data)
        else:
            return super(UserViewSet, self).retrieve(request, pk)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
