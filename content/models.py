from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from user.models import Profile
# from time import strftime

# Create your models here.


class DateClass(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class Category(DateClass):
    category_choices = (
        ("laptop" , "laptops"),
        ("mobile" , "mobile"),
        ("electric_ferniture" , "electric_ferniture")
    )
    name = models.CharField(max_length=50 , choices = category_choices)

    def __str__(self):
        return self.name


class Item(DateClass):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    made_in = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'uploads' ,null = True , blank = True)
    description = models.TextField(blank = True , null = True)
    quantity = models.PositiveIntegerField()
    exist = models.BooleanField()
    price = models.PositiveIntegerField()
    color = ArrayField(models.CharField(max_length = 10))
    of_this_category = models.ForeignKey(Category , verbose_name=("category_relation"), on_delete=models.CASCADE , related_name = 'items' , related_query_name = 'item')
    
    def __str__(self):
        return self.title

class Mobile(Item):
    ram = models.SmallIntegerField()
    touch = models.BooleanField()
    camera = models.CharField(max_length=50)

class laptop(Item):
    ram = models.SmallIntegerField()
    cpu = models.CharField(max_length=50)
    graphic_card = models.CharField(max_length=50)

class Refrigerator(Item):
    side_by_side = models.BooleanField()
    tavan_masrafy = models.CharField(max_length=50)

class WashingMachine(Item):
    tavan_masrafy = models.CharField(max_length=50)

class Cart(DateClass):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='profilecarts', related_query_name='profilecart')
    item = models.ManyToManyField(Item, related_name='carts', related_query_name='cart', through='CartDetailThrough')

    def __str__(self):
        return self.profile.user.username

class CartDetailThrough(models.Model):
    state_choices = (
        ("baught", "baught"),
        ("selected", "selected"),
    )

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartdetails', related_query_name='cartdetail')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cartdetails2', related_query_name='cartdetail2')
    quantity = models.PositiveIntegerField()
    color = ArrayField(models.CharField(max_length = 10))
    state = models.CharField(max_length=20, choices=state_choices)

    def __str__(self):
        return self.cart.profile.user.username

   

# Failed to set 'pythonPath'. Error: Unable to write into folder settings. Please open the 'OnlineShop' folder settings to correct errors/warnings in it and try again.