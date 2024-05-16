from django.db import models
import json
import os

class company_master(models.Model):
    companyname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    mailid=models.CharField(max_length=200)
    state=models.IntegerField()
    district=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    gst=models.CharField(max_length=200)
    

 
class State_Master(models.Model):
    state=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    disc_per=models.CharField(max_length=200)
class ledger(models.Model):
    ledgername=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    mailid=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    gst=models.IntegerField(max_length=200)
    district=models.CharField(max_length=200)
    active=models.CharField(max_length=40)    

    
    
    

# Create your models here.
