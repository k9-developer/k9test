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
    bio = models.TextField(
            'Bio',
            )
    email = models.EmailField()
    
    class Meta:
        pass