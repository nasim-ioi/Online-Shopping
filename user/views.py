from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .models import *
from .serializers import *

# Create your views here.

# TODO : 
# add view to change and update profile

class SingUp(APIView):
    serializer_class = SingUpSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            address = serializer.validated_data.get("address")
            phone = serializer.validated_data.get("phone")
            try : 
                user = User.objects.create(username = username)
            except Exception as e:
                return Response(str(e))
            else:
                # TODO :
                # should create profle with signal
                user.set_password(password)
                token = Token.objects.create(user = user)
                user.save()
                profile = Profile.objects.create(user = user, address = address, phone = phone)
                profile.save()
                return Response("{} profile is created with pasword : {} with token : {}".format(username, password, token.key))

class UserLoginApiview(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



 
