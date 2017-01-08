from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible


from django.db import models
#@python_2_unicode_compatible 
class Description(models.Model):
      desc = models.CharField(max_length = 200,default = "Suits")
      bill = models.FloatField(max_length = 200)
      length = models.FloatField(max_length = 200)
      
      quality = models.CharField( max_length=200,default = "custom")
      rate = models.FloatField(max_length = 200)
      def __str__(self):
        return self.desc

