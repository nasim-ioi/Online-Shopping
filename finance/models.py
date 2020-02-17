from django.db import models
import datetime

# Create your models here.

class Order(models.Model):
    customer_username = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    item_title = models.CharField(max_length=50)
    item_id = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    baught_date = models.DateField(auto_now_add=True)