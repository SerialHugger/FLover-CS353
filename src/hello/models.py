from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=64, null=False)
    password = models.TextField(max_length=64, null=False)
    email = models.TextField(max_length=64, unique=True, null=False)

class User_Phone_Number(models.Model):
    id = models.ForeignKey('User', on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=64,  null=False)
    class Meta:
        unique_together = [['id', 'phone_number']]

class Customer(User):
    

class Seller(User):
    shop_name = models.TextField(max_length=64, unique=True, null=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    address = models.TextField(max_length=64, unique=True, null=False)


class Courier(User):
    city = models.TextField(max_length=64, null = False)
    vehicle = models.TextField(max_length=64)

class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    flower_type = models.TextField(max_length=64, null=False)
    color = models.TextField(max_length=64, null=False)
    occasion = models.TextField(max_length=64, unique=True, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_id = models.IntegerField(null = False)
    description = models.TextField(max_length=256)