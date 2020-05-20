from django.db import models
from django.utils import timezone
# Create your models here.
class Order(models.Model):
    id = models.IntegerField(primary_key=true)
    note = models.CharField(max_length=300)
    price = models.FloatField()
    payment_method = models.CharField(max_length=64)
    date = models.DateTimeField(default=timezone.now)
    est_delivery_time = models.CharField(max_length=64)

class Complaint_Report(models.model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=1023)
    status = models.CharField(max_length=64)
    class Meta:
        unique_together = [['order_id', 'cust_id']]

class Customer_Service_Employee(User):
    shift = models.CharField(max_length=64)

class Forum_Entry(models.Model):
    topic_id = models.ForeignKey(Forum_Topic, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=10000)
    class Meta:
        unique_together = [['topic_id', 'date']]

class Order_Delivery(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_id = models.ForeignKey(Courier, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    class Meta:
        unique_together = [['order_id', 'courier_id', 'seller_id']]

class Stocks(models.Model):
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    sold = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        unique_together = [['flower_id', 'seller_id']]\

class Includes(models.Model):
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    class Meta:
        unique_together = [['flowe_id', 'order_id']]

class Faw_Flow(models.model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    class Meta:
        unique_together = [['cust_id', 'flower_id']]