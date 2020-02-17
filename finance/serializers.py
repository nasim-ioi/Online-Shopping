from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from .models import *


class FinalizeShoppingSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('province', 'city', 'address', 'item_id', 'color', 'quantity')
