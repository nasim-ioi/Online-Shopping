from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from .models import *


class MobileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Mobile
        fields = ('title', 'brand', 'price', 'quantity', 'image', 'detail')

class MobileDetailSerializer(ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('id', 'description', 'color', 'ram', 'touch', 'camera')

class LaptopSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = laptop
        fields = ('title', 'brand', 'price', 'quantity', 'image', 'detail')

class LaptopDetailSerializer(ModelSerializer):
    class Meta:
        model = laptop
        fields = ('id','color', 'quantity', 'description', 'ram', 'cpu', 'graphic_card')

class RefrigeratorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Refrigerator
        fields = ('title', 'brand', 'price', 'quantity', 'image', 'detail')

class RefrigeratorDetailSerializer(ModelSerializer):
    class Meta:
        model = Refrigerator
        fields = ('id', 'description', 'color', 'tavan_masrafy', 'side_by_side')

class WashingMachineSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = WashingMachine
        fields = ('title', 'brand', 'price', 'quantity', 'image', 'detail')

class WashingMachineDetailSerializer(ModelSerializer):
    class Meta:
        model = WashingMachine
        fields = ('id', 'description', 'color', 'tavan_masrafy')

class AddToCartSerializer(ModelSerializer):
    item_id = serializers.CharField(max_length=50, required=True)
    color = serializers.CharField(max_length=100, required=True, help_text="please write only one color")
    class Meta:
        model = Item
        fields = ('item_id', 'color', 'quantity')

class ItemDetailSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('title',)

class ShowCartSerializer(ModelSerializer):
    item = ItemDetailSerializer(many = False)
    class Meta:
        model = CartDetailThrough
        fields = ('item', 'quantity', 'color', 'state')

