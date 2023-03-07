from django.contrib.auth.models import User, Group

from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(serializers, HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url','usrername','email','groups']


class GroupSerializer(serializers, HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']