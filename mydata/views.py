# coding: utf-8
# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from k9test.mydata.models import MyData 

def index_view(request):
    my_data = get_object_or_404(MyData, pk = 1)
    variables = RequestContext(request, {
        'my_data': my_data,
    })
    return render_to_response(
        'index.html',
        variables
    )