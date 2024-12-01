from django.db import models
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    name = models.CharField(max_length=255)
    dollars = models.SmallIntegerField()
    cents = models.SmallIntegerField()
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Countdown_Product(models.Model):
    name = models.CharField(max_length=255)
    dollars = models.SmallIntegerField()
    cents = models.SmallIntegerField()
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class ShoppingList(models.Model):
    user = models.CharField(max_length=255)
    contents = models.CharField(max_length=255)

        