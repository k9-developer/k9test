#coding: utf - 8
 
from django.contrib import admin
from k9test.mydata.models import MyData



 
class MyDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyData, MyDataAdmin)


