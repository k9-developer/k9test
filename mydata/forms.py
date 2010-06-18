# coding: utf-8

from django import forms
from k9test.mydata.models import MyData


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('/media/css/jquery.ui.all.css', )
        }
        js = ('/media/js/ui/jquery.ui.core.js', '/media/js/ui/jquery.ui.widget.js', 
              '/media/js/ui/jquery.ui.datepicker.js')


class MyDataForm(forms.ModelForm):
    birthday = forms.DateField(widget=CalendarWidget)
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': '17', 'rows': '5'} ,))

    class Meta:
        model = MyData
        fields = ['email', 'bio', 'birthday', 'last_name', 'name', ]