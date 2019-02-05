from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User


class UserSerializer(ModelSerializer):
    """[summary]

    Arguments:
        ModelSerializer {[type]} -- [description]
    """

    class Meta:
        model = User
        exclude = ('password',)
