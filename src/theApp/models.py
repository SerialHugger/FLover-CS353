from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    username = models.TextField(max_length=64, null=False)
    password = models.TextField(max_length=64, null=False)
    email = models.TextField(max_length=64, unique=True, null=False)
    class Meta:
        app_label = 'theApp'

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    note = models.CharField(max_length=300)
    price = models.FloatField()
    payment_method = models.CharField(max_length=64)
    date = models.DateTimeField(default=timezone.now)
    est_delivery_time = models.CharField(max_length=64)
    class Meta:
        app_label = 'theApp'
class Complaint_Report(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=1023)
    status = models.CharField(max_length=64)
    class Meta:
        unique_together = [['order_id', 'cust_id']]
        app_label = 'theApp'
class Customer_Service_Employee(User):
    shift = models.CharField(max_length=64)
    class Meta:
        app_label = 'theApp'

class Forum_Topic(models.Model):
    topic_id = models.CharField(max_length=64, verbose_name="topic_id",primary_key=True)
    date = models.DateTimeField(default=timezone.now) #netten baktım yanlış olabilir
    title = models.CharField(max_length=64, verbose_name="title")
    category = models.CharField(max_length=64, verbose_name="category")
    no_of_entries = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta():
        app_label = 'theApp'

class Forum_Entry(models.Model):
    topic_id = models.ForeignKey(Forum_Topic, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=10000)
    class Meta:
        unique_together = [['topic_id', 'date']]
        app_label = 'theApp'

class Courier(User):
    city = models.TextField(max_length=64, null = False)
    vehicle = models.TextField(max_length=64)
    class Meta:
        app_label = 'theApp'

class Seller(User):
    shop_name = models.TextField(max_length=64, unique=True, null=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    address = models.TextField(max_length=64, unique=True, null=False)
    class Meta:
        app_label = 'theApp'


class Order_Delivery(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_id = models.ForeignKey(Courier, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    class Meta:
        unique_together = [['order_id', 'courier_id', 'seller_id']]
        app_label = 'theApp'


class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    flower_type = models.TextField(max_length=64, null=False)
    color = models.TextField(max_length=64, null=False)
    occasion = models.TextField(max_length=64, unique=True, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_id = models.IntegerField(null = False)
    description = models.TextField(max_length=256)
    category = models.CharField(max_length=64, verbose_name="category")
    class Meta:
        app_label = 'theApp'


class Stocks(models.Model):
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    sold = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        unique_together = [['flower_id', 'seller_id']]
        app_label = 'theApp'

class Includes(models.Model):
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    class Meta:
        unique_together = [['flower_id', 'order_id']]
        app_label = 'theApp'

class Customer(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    class Meta:
        app_label = 'theApp'


class Faw_Flow(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    class Meta:
        unique_together = [['cust_id', 'flower_id']]
        app_label = 'theApp'

class User_Phone_Number(models.Model):
    User_id = models.ForeignKey('User', on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=64,  null=False)
    class Meta:
        unique_together = [['User_id', 'phone_number']]
        app_label = 'theApp'

'''
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
'''

class Chocolate (models.Model):
    chocolate_type = models.CharField(max_length=64, verbose_name="chocolate_type",primary_key=True)
    price = models.FloatField()
    price = models.IntegerField()
    class Meta():
        app_label = 'theApp'

class Attached (models.Model):
    Order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    attached_type = models.ForeignKey(Chocolate, on_delete=models.CASCADE)
    no_of_entries = models.IntegerField()
    #FOREIGN KEY NASI PRIMARY OLACAK BUNA BAK
    class Meta():
        unique_together = [['Order_id' , 'attached_type']]
        app_label = 'theApp'

class Fav_shop(models.Model):


    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE) 
    class Meta():
        unique_together = [['customer_id' , 'seller_id']]
        app_label = 'theApp'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ad")
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        app_label = 'theApp'
