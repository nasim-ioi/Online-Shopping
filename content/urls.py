from django.urls import path , include
from django.conf.urls import url
from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter


router = DefaultRouter()
# router.register(r'categories', CategoryViewset)
router.register(r'mobile', MobileViewset)
router.register(r'laptop', LaptopViewset)
router.register(r'Refrigerator', RefrigeratorViewset)
router.register(r'WashingMachine', WashingMachineViewset)
router.register(r'show_cart', ShowCart, basename='ShowCart')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('add_to_cart', AddToCart.as_view()),
]

