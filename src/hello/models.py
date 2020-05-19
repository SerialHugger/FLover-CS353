from django.db import models
from django.utils import timezone
# Create your models here.
class Chocolate (models.Model):
    chocolate_type = models.CharField(max_length=64, verbose_name="chocolate_type",primary_key=True)
    price = models.FloatField()
    price = models.IntegerField()

class Forum_topic (models.Model):
    topic_id = models.CharField(max_length=64, verbose_name="topic_id",primary_key=True)
    date = models.DateTimeField(default=timezone.now) #netten baktım yanlış olabilir
    title = models.CharField(max_length=64, verbose_name="title")
    category = models.CharField(max_length=64, verbose_name="category")
    no_of_entries = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Attached (models.Model):
    id = models.ForeignKey(Order, on_delete=models.CASCADE)
    attached_type = models.ForeignKey(Chocolate, on_delete=models.CASCADE)
    no_of_entries = models.IntegerField()
    #FOREIGN KEY NASI PRIMARY OLACAK BUNA BAK
    class Meta():
        unique_together = [['id' , 'attached_type']]

class Fav_shop():

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE) 
    class Meta():
        unique_together = [['customer_id' , 'seller_id']]



