from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class MyCart(models.Model):
    user       = models.ForeignKey(User, on_delete= models.CASCADE)
    products   = models.ManyToManyField(Product)