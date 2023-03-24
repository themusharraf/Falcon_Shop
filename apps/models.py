from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Status(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CLIENT = 'client', 'Client'
        VIP_CLIENT = 'vip_client', 'Vip client'

    status = models.CharField(max_length=50, choices=Status.choices, default=Status.CLIENT)
    email = models.EmailField(unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    shopping_cost = models.SmallIntegerField(default=0)
    tags = models.ForeignKey('apps.Tag', models.CASCADE,blank=True,default=1)
    specification = models.JSONField(default=dict, blank=True)
    author = models.ForeignKey('apps.User', models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey('apps.Product', models.CASCADE)
    image = models.ImageField(upload_to='product/images/')
