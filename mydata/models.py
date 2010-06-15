# coding: utf-8
from django.db import models

class MyData(models.Model):
    name = models.CharField(
            'Name',
            max_length=20,
            )
    last_name = models.CharField(
            'Last Name',
            max_length=20,
            )
    birthday = models.DateField()
    bio = models.TextField(
            'Bio',
            )
    email = models.EmailField()
    
    class Meta:
        pass
    
class HttpReq(models.Model):
    path = models.CharField(
            'Path',
            max_length=200,
            )
    time = models.DateTimeField(
            'Time',
            auto_now_add=True,
            )
    
    class Meta:
        pass