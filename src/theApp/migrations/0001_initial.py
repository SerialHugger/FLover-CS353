# Generated by Django 3.0.6 on 2020-05-20 19:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ad')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('chocolate_type', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='chocolate_type')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('flower_type', models.TextField(max_length=64)),
                ('color', models.TextField(max_length=64)),
                ('occasion', models.TextField(max_length=64, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo_id', models.IntegerField()),
                ('description', models.TextField(max_length=256)),
                ('category', models.CharField(max_length=64, verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('payment_method', models.CharField(max_length=64)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('est_delivery_time', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=64)),
                ('password', models.TextField(max_length=64)),
                ('email', models.TextField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='theApp.User')),
                ('city', models.TextField(max_length=64)),
                ('vehicle', models.TextField(max_length=64)),
            ],
            bases=('theApp.user',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='theApp.User')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
            bases=('theApp.user',),
        ),
        migrations.CreateModel(
            name='Customer_Service_Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='theApp.User')),
                ('shift', models.CharField(max_length=64)),
            ],
            bases=('theApp.user',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='theApp.User')),
                ('shop_name', models.TextField(max_length=64, unique=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('address', models.TextField(max_length=64, unique=True)),
            ],
            bases=('theApp.user',),
        ),
        migrations.CreateModel(
            name='Forum_Topic',
            fields=[
                ('topic_id', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='topic_id')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('category', models.CharField(max_length=64, verbose_name='category')),
                ('no_of_entries', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Phone_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.TextField(max_length=64)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.User')),
            ],
            options={
                'unique_together': {('User_id', 'phone_number')},
            },
        ),
        migrations.CreateModel(
            name='Includes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('flower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Flower')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Order')),
            ],
            options={
                'unique_together': {('flower_id', 'order_id')},
            },
        ),
        migrations.CreateModel(
            name='Forum_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.CharField(max_length=10000)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Forum_Topic')),
            ],
            options={
                'unique_together': {('topic_id', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Complaint_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1023)),
                ('status', models.CharField(max_length=64)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.User')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Order')),
            ],
            options={
                'unique_together': {('order_id', 'cust_id')},
            },
        ),
        migrations.CreateModel(
            name='Attached',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_entries', models.IntegerField()),
                ('Order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Order')),
                ('attached_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Chocolate')),
            ],
            options={
                'unique_together': {('Order_id', 'attached_type')},
            },
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold', models.IntegerField()),
                ('count', models.IntegerField()),
                ('flower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Flower')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Seller')),
            ],
            options={
                'unique_together': {('flower_id', 'seller_id')},
            },
        ),
        migrations.CreateModel(
            name='Order_Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=64)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Order')),
                ('courier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Courier')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Seller')),
            ],
            options={
                'unique_together': {('order_id', 'courier_id', 'seller_id')},
            },
        ),
        migrations.CreateModel(
            name='Faw_Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Flower')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Customer')),
            ],
            options={
                'unique_together': {('cust_id', 'flower_id')},
            },
        ),
        migrations.CreateModel(
            name='Fav_shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Customer')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theApp.Seller')),
            ],
            options={
                'unique_together': {('customer_id', 'seller_id')},
            },
        ),
    ]