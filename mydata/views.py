# coding: utf-8
# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from k9test.mydata.models import MyData, HttpReq
from k9test.mydata.forms import MyDataForm


def index_view(request):
    my_data = get_object_or_404(MyData, pk=1)
    variables = RequestContext(request, {
        'my_data': my_data,
        })
    return render_to_response(
        'index.html',
        variables
        )

def httplist_view(request):
    httplist = HttpReq.objects.order_by("id").all()[:10]
    zero_count = float(HttpReq.objects.filter(priority__exact=0).count())
    one_count = float(HttpReq.objects.filter(priority__exact=1).count())
    all_count = float(HttpReq.objects.count())
    p_zero = zero_count/all_count*100.00
    p_one = one_count/all_count*100.00
    variables = RequestContext(request, {
        'httplist': httplist,
        'p_zero': p_zero,
        'p_one': p_one,
        'c_zero': int(zero_count),
        'c_one': int(one_count),
        'all_count' : int(all_count),
        })
    return render_to_response(
        'list_http.html',
        variables
        )

@login_required
def mydata_edit(request):
    my_data = get_object_or_404(MyData, pk=1)
    if request.method == 'POST':
        my_data_form = MyDataForm(data=request.POST, instance=my_data)
        if my_data_form.is_valid():
            my_data_form.save()
            return HttpResponseRedirect(reverse(index_view))
    else:
        my_data_form = MyDataForm(instance=my_data)

    variables = RequestContext(request, {
        #'my_data': my_data,
        'my_data_form': my_data_form,
        })
    return render_to_response(
        'mydata_edit.html',
        variables
        )

@login_required
def mydata_ajax_edit_form(request):
    my_data = get_object_or_404(MyData, pk=1)
    if request.method == 'POST':
        my_data_form = MyDataForm(data=request.POST, instance=my_data)
        if my_data_form.is_valid():
            my_data_form.save()
            #return HttpResponseRedirect('/')
    else:
        my_data_form = MyDataForm(instance=my_data)

    variables = RequestContext(request, {
        'my_data_form': my_data_form,
        })
    return render_to_response(
        'ajax/mydata_edit_form.html',
        variables
        )