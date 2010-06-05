#coding: utf - 8
 
from django.contrib import admin
from k9test.mydata.models import MyData, HttpReq



 
class MyDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyData, MyDataAdmin)
admin.site.register(HttpReq)


