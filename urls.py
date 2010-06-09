# coding: utf-8
from django.conf.urls.defaults import *
from django.conf import settings

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
    (r'^ajax/mydata/edit/$', 'k9test.mydata.views.mydata_ajax_edit_form'),
    
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        #{'template_name': 'accounts/login.html',
        #}
        ),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/',
        }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
