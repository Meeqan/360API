from rest_framework import serializers
from vendors.models import Vendor
from users.models import User
from users.api.serializers import UserSerializer


class VendorSerializer(serializers.ModelSerializer):
    """[summary]

    Arguments:
        ModelSerializer {[type]} -- [description]
    """
    owner = UserSerializer()


    class Meta:
        model = Vendor
        fields = ('id', 'name', 'location', 'description',
                  'owner_id', 'logo', 'phone', 'email', 'owner')
