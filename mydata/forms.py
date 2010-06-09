# coding: utf-8

from django import forms
from k9test.mydata.models import MyData
from django.forms.extras.widgets import SelectDateWidget

class MyDataForm(forms.ModelForm):
    birthday = forms.DateField(widget=SelectDateWidget(years=xrange(1950, 2000)))
    class Meta:
        model = MyData
        fields = ['email', 'bio', 'birthday', 'last_name', 'name', ]

