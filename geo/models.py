from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Hornet(models.Model):

    name = models.CharField(max_length=200,default='New test post Individual')
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    email = models.CharField(max_length=200,default='Anonymous')
    ip=models.CharField(max_length=200,default='Noip')
    pub_dtime = models.DateTimeField(default=timezone.now)
    view_dtime = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.name

class HornetNode(models.Model):
    
    name = models.CharField(max_length=200,default='New test post NODE')
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name

    
        
