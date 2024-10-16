from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    dollars = models.SmallIntegerField()
    cents = models.SmallIntegerField()
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    # def __init__(self, _name, _dollars, _cents, _img, _link):
    #     self.name = _name
    #     self.dollars = _dollars
    #     self.cents = _cents
    #     self.img = _img
    #     self.link = _link


        