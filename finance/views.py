from django.shortcuts import render
from rest_framework.response import Response
from .models import * 
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import *
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.decorators import action
from user import models
from content.models import Item
import datetime
import random

# Create your views here.

# TODO :
# should add feature to cart that can shop product directly from cart

class FinalizeShopping(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = FinalizeShoppingSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception = True):
            username = request.user.username
            phone = request.user.profile.phone
            item_id = serializer.validated_data.get("item_id")
            color_wanted = serializer.validated_data.get("color")
            quantity_wanted = serializer.validated_data.get("quantity")
            try : 
                item = Item.objects.get(id = item_id)
            except Exception as e:
                return Response(str(e))
            else:
                try :
                    cart = request.user.profile.profilecarts.get()
                    cartdetailthrog = cart.cartdetails.get(item = item)
                except Exception as e:
                    return Response("you should first add this item to yor cart as error is : {}".format(str(e)))
                item_title = item.title
                if color_wanted not in item.color:
                    return Response("this color is not exist for {}".format(item.title,))
                elif item.quantity < quantity_wanted:
                    return Response("we do not have enough {}".format(item.title,))
                else:
                    result = paymentShopping() # dargah pardakht -> what arguments should pass? -> how to identify user? 
                    # -> token generation? -> return True or return False
                    if not result:
                        return Response("UNSECCESSFUL SHOPPING")
                    else:
                        orderInvoicing(result, username, item_title, phone, serializer.validated_data)
                        item.quantity -= quantity_wanted
                        item.save()
                        cartdetailthrog.state = "baught"
                        cartdetailthrog.save()
                        return Response("SUCCESSFUL SHOPPING")

def paymentShopping():
    ran = [0, 1, 1, 1]
    return(random.choice(ran))

def orderInvoicing(result, username, item_title, phone, info):
    order = Order.objects.create(customer_username=username, province=info["province"], city=info["city"], address=info["address"], phone=phone, item_title=item_title, item_id=info["item_id"], color=info["color"], quantity=info["quantity"])

class ShowOrder(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FinalizeShoppingSerializer
    def get_queryset(self):
        return Order.objects.filter(customer_username = self.request.user.username)

class ShowTodayOrders(ReadOnlyModelViewSet):
    today_date = datetime.date.today()
    permission_classes = [IsAuthenticated]
    serializer_class = FinalizeShoppingSerializer
    def get_queryset(self):
        return Order.objects.filter(baught_date = today_date)

