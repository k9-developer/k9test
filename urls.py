# coding: utf-8
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^k9test/', include('k9test.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'k9test.mydata.views.index_view'),
    (r'^mydata/edit/$', 'k9test.mydata.views.mydata_edit'),
    
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        #{'template_name': 'accounts/login.html',
        #}
        ),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/',
        }),
)
