# coding: utf-8
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
import os
from django.test import TestCase
from django.db import IntegrityError
from django.test.client import Client
from k9test.mydata.models import HttpReq, MyData, Logging
import datetime
import sys


class CommandTest(TestCase):
    """ Test command: printlist"""

    def testCommandPrintlist(self):
        cmd = 'manage.py printlist'
        if sys.platform != "win32":
            cmd = 'python manage.py printlist' 
        fin, fout, ferr = os.popen3(cmd)
        result = fout.read()
        err = ferr.read()
        self.failUnlessEqual(err, "", "Command not runing!")
        self.failIfEqual(result, "")


class ViewsTest(TestCase):
    """ Test views"""

    def testIndexPage(self):
        client = Client()
        response = client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['my_data'], None)

    def testSettingsView(self):
        client = Client()
        response = client.get('/')
        self.failIfEqual(response.context['settings'], None)

    def testMydataForm(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/mydata/edit/')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['my_data_form'], None)

    def testMydataAjaxForm(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/ajax/mydata/edit/')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['my_data_form'], None)

    def testHttpListView(self):
        client = Client()
        response = client.get('/httplist/')
        self.failUnlessEqual(response.status_code, 200)
        ht_list = response.context['httplist']
        ht_count = HttpReq.objects.count()
        self.failIfEqual(ht_list, None)
        self.failUnlessEqual(len(ht_list), 9)
        self.failUnlessEqual(ht_count, 9)
        for ht in ht_list:
            self.failIf(ht.id>10, "id lt 10")
        response = client.get('/httplist/')
        self.failUnlessEqual(response.status_code, 200)
        ht_list = response.context['httplist']
        ht_count = HttpReq.objects.count()
        self.failIfEqual(ht_list, None)
        self.failUnlessEqual(len(ht_list), 10)
        self.failUnlessEqual(ht_count, 10)
        for ht in ht_list:
            self.failIf(ht.id>10, "id lt 10")
        response = client.get('/httplist/')
        self.failUnlessEqual(response.status_code, 200)
        ht_list = response.context['httplist']
        ht_count = HttpReq.objects.count()
        self.failIfEqual(ht_list, None)
        self.failUnlessEqual(len(ht_list), 10)
        self.failUnlessEqual(ht_count, 11)
        for ht in ht_list:
            self.failIf(ht.id>10, "id lt 10")

class ModelsTest(TestCase):
    """ Test models"""

    def testHttpObjectSave(self):
        dt_now = datetime.datetime(2010, 06, 10, 22, 45, 10)
        h = HttpReq()
        h.path = u"/accounts/login/"
        h.time = dt_now
        h.priority = 1
        h.save()
        #self.assertRaises(IntegrityError, h.save())
        self.failUnlessEqual(h.path, u"/accounts/login/")
        self.failUnlessEqual(h.time, dt_now)
        self.failUnlessEqual(h.priority, 1)

    def testHttpObjectNew(self):
        ht_count = HttpReq.objects.count()
        client = Client()
        response = client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        ht_count2 = HttpReq.objects.count()
        self.failUnlessEqual(ht_count + 1, ht_count2)

class SignalsTest(TestCase):
    """ Test signsls"""

    def testSignalsMyData(self):
        """Do Test Signals on MyData """

        time = datetime.datetime.now()
        md = MyData.objects.get(pk=1)
        md_id = md.id
        md.delete()
        log = Logging.objects.filter(object_repr='mydata', \
            object_id=md_id, action = 'deleted', action_time__gte=time).count()
        self.failUnlessEqual(log, 1)
        time = datetime.datetime.now()
        md = MyData(name="Igor", last_name="Savchenko", \
            birthday="1983-06-16", bio="was born", email="k9@inet.ua")
        md.save()
        md_id = md.id
        log = Logging.objects.filter(object_repr='mydata', \
            object_id=md_id, action = 'created', action_time__gte=time).count()
        self.failUnlessEqual(log, 1)
        time = datetime.datetime.now()
        md.bio="in Kherson"
        md.save()
        log = Logging.objects.filter(object_repr='mydata', \
            object_id=md_id, action = 'edited', action_time__gte=time).count()
        self.failUnlessEqual(log, 1)

    def testSignalsHttpReq(self):
        """Do Test Signals on HttpReq """

        time = datetime.datetime.now()
        md = HttpReq.objects.all()[:1].get()
        md_id = md.id
        md.delete()
        log = Logging.objects.filter(object_repr='httpreq', \
            object_id=md_id, action = 'deleted', action_time__gte=time).count()
        self.failUnlessEqual(log, 1)
        time = datetime.datetime.now()
        md = HttpReq(path="/", time="2010-06-16 14:00:05")
        md.save()
        md_id = md.id
        log = Logging.objects.filter(object_repr='httpreq', \
            object_id=md_id, action = 'created', action_time__gte=time).count()
        self.failUnlessEqual(log, 1)
        time = datetime.datetime.now()
        md.priority=1
        md.save()
        log = Logging.objects.filter(object_repr='httpreq', \
            object_id=md_id, action = 'edited', action_time__gte=time).count()
        self.failUnlessEqual(log, 1)