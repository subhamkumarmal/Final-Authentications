from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import Settings
# Create your models here.

class Students(models.Model):
    sname=models.CharField(max_length=30)
    sage=models.IntegerField()
    semail=models.EmailField()


    class Meta:
        db_table='student'


