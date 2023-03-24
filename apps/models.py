from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import EmailField


class User(AbstractUser):
    email = EmailField(unique=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    shop_cost = models.IntegerField()
    tags = models.TextField(blank=True, null=True)
    specification = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'

    def __str__(self):
        return self.name
