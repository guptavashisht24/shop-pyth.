'''model
'''
from __future__ import unicode_literals
#from django.utils.encoding import python_2_unicode_compatible


from django.db import models
#@python_2_unicode_compatible
class Description(models.Model):
    id = models.BigAutoField(primary_key=True)
    desc = models.CharField(max_length=200, default="Suits")
    bill = models.FloatField(max_length=200)
    length = models.FloatField(max_length=200)
    quality = models.CharField(max_length=200, default="custom")
    rate = models.FloatField(max_length=200)

    def __str__(self):
        return self.desc+","+self.quality+","+str(self.rate)

class Bill(models.Model):
    id = models.BigAutoField(primary_key=True)
    party = models.CharField(max_length=200, default="none")
    phone = models.BigIntegerField(default = 0)
    invoice = models.FloatField(max_length=200)
    amount = models.FloatField(max_length=200)
    bill_name = models.CharField(max_length=200, default="none")

    def __str__(self):
        return self.party+','+str(self.invoice)+','+str(self.amount)+','+self.bill_name

    def bill_id(self):
        return self.id

class Customer(models.Model):
    name = models.CharField(max_length=200, default="none")
    phone = models.BigIntegerField(primary_key=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name+','+str(self.phone)+','+str(self.email)

class Sale(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_id = models.CharField(max_length=1000)
    length = models.CharField(max_length=1000)
    cust_id = models.BigIntegerField()
    discount = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)

    def __str__(self):
        return self.item_id+":"+self.length

class Discount(models.Model):
    value = models.IntegerField(default = 0, primary_key=True)
    count = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.value)+","+str(self.count)
