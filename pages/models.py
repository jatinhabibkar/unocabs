from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Ride(models.Model):

    def getname(thename):
        return thename.split(',')[0]

    rider = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    customerId=models.IntegerField(default=-1)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    tel = models.IntegerField(default=000-000-0000)
    cost = models.IntegerField()
    message = models.CharField(max_length=200)
    vehicle = models.CharField(max_length=20)
    applied =models.TextField(null=True)
    sourName = models.CharField(max_length=500)
    Scordlog = models.DecimalField(decimal_places=6,max_digits=13)
    Scordlat = models.DecimalField(decimal_places=6,max_digits=13)

    destName = models.CharField(max_length=500)
    Dcordlog = models.DecimalField(decimal_places=6,max_digits=13)
    Dcordlat = models.DecimalField(decimal_places=6,max_digits=13)
    Rdate = models.DateField()
    Rtime = models.TimeField()

    step1 = models.BooleanField(default=False)
    step2 = models.BooleanField(default=False)
    step3 = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    



    




    
    




    

