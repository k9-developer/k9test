#coding: utf - 8
 
from django.contrib import admin
from k9test.mydata.models import MyData, HttpReq, Logging



 
class MyDataAdmin(admin.ModelAdmin):
    pass

class HttpReqAdmin(admin.ModelAdmin):
    list_filter = ('priority',)

admin.site.register(MyData, MyDataAdmin)
admin.site.register(HttpReq, HttpReqAdmin)
admin.site.register(Logging)


