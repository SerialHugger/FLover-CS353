from django.db import models
from django.utils import timezone
from django.db import connection
# Create your models here.

class myUser(models.Model):
    username = models.TextField(max_length=64, null=False)
    password = models.TextField(max_length=64, null=False)
    email = models.TextField(max_length=64, unique=True, null=False)
    userType = models.TextField(max_length=64, null=False)
    #userTypeID = models.TextField(max_length=64, null=False)

    class Meta:
        app_label = 'theApp'

    def save(dataDic, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute(' INSERT INTO theApp_myuser(username,password,email,userType) VALUES(%s,%s,%s,%s)', [dataDic['username'],dataDic['password'],dataDic['email'],dataDic['userType']])
        print(' success')

    def set_password(psd):
        password = psd

class Order(models.Model):
    note = models.CharField(max_length=300)
    price = models.FloatField()
    payment_method = models.CharField(max_length=64)
    date = models.DateTimeField(default=timezone.now)
    est_delivery_time = models.CharField(max_length=64)
    class Meta:
        app_label = 'theApp'

    def save(note,price,payment_method):
        datDict = {"note" : note,  "price": price , "payment_method": payment_method , "date" : timezone.now , "est_delivery_time":"1"} 
        cursor.execute(' INSERT INTO theApp_order(note,price,payment_method,date,est_delivery_time) VALUES(%s,%s,%s,%s,%s)', [dataDic['note'],dataDic['price'],dataDic['payment_method'],dataDic['date'],dataDic['est_delivery_time']])

class Complaint_Report(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(myUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=1023)
    status = models.CharField(max_length=64)
    class Meta:
        unique_together = [['order_id', 'cust_id']]
        app_label = 'theApp'

class Customer_Service_Employee(myUser):
    shift = models.CharField(max_length=64)
    class Meta:
        app_label = 'theApp'

class Forum_Topic(models.Model):
    topic_id = models.CharField(max_length=64, verbose_name="topic_id",primary_key=True)
    date = models.DateTimeField(default=timezone.now) #netten baktım yanlış olabilir
    title = models.CharField(max_length=64, verbose_name="title")
    category = models.CharField(max_length=64, verbose_name="category")
    no_of_entries = models.IntegerField()
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    class Meta():
        app_label = 'theApp'

class Forum_Entry(models.Model):
    topic_id = models.ForeignKey(Forum_Topic, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=10000)
    class Meta:
        unique_together = [['topic_id', 'date']]
        app_label = 'theApp'

class Courier(myUser):
    city = models.TextField(max_length=64, null = False)
    vehicle = models.TextField(max_length=64)
    class Meta:
        app_label = 'theApp'

class Seller(myUser):
    shop_name = models.TextField(max_length=64, unique=True, null=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    address = models.TextField(max_length=64, unique=True, null=False)

    class Meta:
        app_label = 'theApp'
    def save(dataDic, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute(' INSERT INTO theApp_seller(username,password,email,userType) VALUES(%s,%s,%s,%s)', [dataDic['username'],dataDic['password'],dataDic['email'],dataDic['userType']])
        print(' success')


class Order_Delivery(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_id = models.ForeignKey(Courier, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    class Meta:
        unique_together = [['order_id', 'courier_id', 'seller_id']]
        app_label = 'theApp'


class Flower(models.Model):
    flower_id = models.IntegerField(primary_key=True)
    flower_type = models.TextField(max_length=64, null=False)
    color = models.TextField(max_length=64, null=False)
    occasion = models.TextField(max_length=64, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField(null = False, default=0)
    photo_id = models.IntegerField(null = False)
    description = models.TextField(max_length=256)
    category = models.CharField(max_length=64, verbose_name="category")
    class Meta:
        app_label = 'theApp'
    
    def save(dataDic, *args, **kwargs):
        cursor = connection.cursor()
        print("cate :", dataDic['category'])
        if(str(dataDic['category']) == "1"):
            dataDic['category'] = 'plastic'
        elif(str(dataDic['category']) == "2"):
            dataDic['category'] = 'focal'
        elif(str(dataDic['category']) == "3"):
            dataDic['category'] = 'filler'
        elif(str(dataDic['category']) == "4"):
            dataDic['category'] = 'line'
        print("cate :", dataDic['category'])
        cursor.execute('INSERT INTO theApp_flower(flower_type,color,occasion,price,stock_count,photo_id,description,category) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', [dataDic['flower_type'],dataDic['color'],dataDic['occasion'],dataDic['price'],dataDic['stock_count'],dataDic['photo_id'],dataDic['description'],dataDic['category']])
        print('success')
        fid = cursor.execute('Select flower_id FROM theApp_flower Where photo_id = %s', [dataDic['photo_id']]).fetchall()[0][0]
        return fid

    def delete(name, flo_id, *args, **kwargs):
        cursor = connection.cursor()
        print(name)
        cursor.execute('DELETE FROM theApp_stocks WHERE flower_id_id = %s', [flo_id])
        cursor.execute('DELETE FROM theApp_flower WHERE flower_type = %s', [name])

    def changePrice(name, price, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute('UPDATE theApp_flower SET price = %s WHERE flower_type = %s', [price, name])


class Stocks(models.Model):
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(myUser, on_delete=models.CASCADE)
    sold = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        unique_together = [['flower_id', 'seller_id']]
        app_label = 'theApp'

    def save(dataDic, *args, **kwargs):
        print("FROM SELLER BOII:",dataDic)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO theApp_stocks(sold,count,flower_id_id,seller_id_id) VALUES(%s,%s,%s,%s)', [dataDic['sold'],dataDic['count'],dataDic['flower_id'],dataDic['seller_id']])
        print('success')
    


class Includes(models.Model):
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    class Meta:
        unique_together = [['flower_id', 'order_id']]
        app_label = 'theApp'

class Customer(myUser):
    user = models.OneToOneField(myUser, on_delete=models.CASCADE, parent_link=True)
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
    phone_id = models.ForeignKey(myUser, on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=64,  null=False)
    class Meta:
        unique_together = [['phone_id', 'phone_number']]
        app_label = 'theApp'

'''
@receiver(post_save, sender=myUser)
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

    def save(dataDic, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute('INSERT INTO theApp_category(name) VALUES(%s)', [dataDic['name']])
        print('success')