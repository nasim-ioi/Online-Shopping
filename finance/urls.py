from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'show_orders', ShowOrder, basename='ShowOrder')
router.register(r'show_today_orders', ShowTodayOrders, basename='ShowTodayOrders')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('finalize_shopping/', FinalizeShopping.as_view()),
]
