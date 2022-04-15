# Generated by Django 4.0.3 on 2022-03-19 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cName', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('cEmail', models.EmailField(max_length=254)),
                ('cLogo', models.ImageField(blank=True, upload_to='images')),
                ('cUrl', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/EmployeProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('feedback', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=50, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.customer')),
                ('employes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.employes')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.product')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eFname', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('eLname', models.CharField(max_length=50)),
                ('eEmail', models.EmailField(max_length=254)),
                ('ePhone', models.CharField(max_length=50)),
                ('eCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.company')),
            ],
        ),
    ]