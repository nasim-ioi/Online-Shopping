from django.shortcuts import render
from rest_framework.response import Response
from .models import * 
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.decorators import action

# Create your views here.

# TODO :
# add view to change and update cart

class MobileViewset(ReadOnlyModelViewSet):
    queryset = Mobile.objects.all()
    serializers = {
            'list' : MobileSerializer,
            'retrieve' : MobileDetailSerializer
        }
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'brand')
    def get_serializer_class(self):
        return self.serializers.get(self.action)

class LaptopViewset(ReadOnlyModelViewSet):
    queryset = laptop.objects.all()
    serializers = {
            'list' : LaptopSerializer,
            'retrieve' : LaptopDetailSerializer
        }
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'brand')
    def get_serializer_class(self):
        return self.serializers.get(self.action)

class RefrigeratorViewset(ReadOnlyModelViewSet):
    queryset = Refrigerator.objects.all()
    serializers = {
            'list' : RefrigeratorSerializer,
            'retrieve' : RefrigeratorDetailSerializer
        }
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'brand')
    def get_serializer_class(self):
        return self.serializers.get(self.action)
    
class WashingMachineViewset(ReadOnlyModelViewSet):
    queryset = WashingMachine.objects.all()
    serializers = {
            'list' : WashingMachineSerializer,
            'retrieve' : WashingMachineDetailSerializer
        }
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'brand')
    def get_serializer_class(self):
        return self.serializers.get(self.action)

class AddToCart(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = AddToCartSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            # AnonymousUser
            # item_category = serializer.validated_data.get("name_of_category")
            item_id = serializer.validated_data.get("item_id")
            color_wanted = serializer.validated_data.get("color")
            quantity_wanted = serializer._validated_data.get("quantity")
            try:
                item = Item.objects.get(id = item_id)
                # item = item_category.objects.get(id = item_id)
            except Exception as e:
                return Response(str(e))
            else:
                list_of_color = item.color
                quantity = item.quantity
                item_title = item.title
                if color_wanted not in list_of_color:
                    return Response("this color is not exist for {}".format(item_title,))
                elif quantity < quantity_wanted:
                    return Response("we do not have enough {}".format(item_title,))
                else:
                    try:
                        cart = Cart.objects.get(profile = user.profile)
                    except:
                        cart = Cart.objects.create(profile = user.profile)
                    else:
                        cartdetailthrough = CartDetailThrough.objects.create(cart=cart, item=item, quantity=quantity_wanted, color=[color_wanted], state='selected')
                        return Response("{} added to your cart succesfully".format(item_title))

class ShowCart(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated] 
    serializer_class = ShowCartSerializer
    def get_queryset(self):
        cart = self.request.user.profile.profilecarts.get()
        return cart.cartdetails.all()
   


