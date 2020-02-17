from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from .models import *

class SingUpSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"), required=True)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        required=True
    )
    address = serializers.CharField(max_length=100, required=True)
    phone = serializers.CharField(max_length=20, required=True)