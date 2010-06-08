# coding: utf-8
# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from k9test.mydata.models import MyData
from k9test.mydata.forms import MyDataForm


def index_view(request):
    my_data = get_object_or_404(MyData, pk = 1)
    variables = RequestContext(request, {
        'my_data': my_data,
    })
    return render_to_response(
        'index.html',
        variables
    )
 

def mydata_edit(request):
    my_data = get_object_or_404(MyData, pk = 1)
    if request.method == 'POST':
        my_data_form = MyDataForm(data = request.POST, instance = my_data)
        if my_data_form.is_valid():
            my_data_form.save()
            return HttpResponseRedirect('/')
    else:
        my_data_form = MyDataForm(instance = my_data)

    variables = RequestContext(request, {
        #'my_data': my_data,
        'my_data_form': my_data_form,
    })
    return render_to_response(
        'mydata_edit.html',
        variables
    )