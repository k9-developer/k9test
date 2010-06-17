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
from k9test.mydata.models import HttpReq
import datetime
import sys


class SimpleTest(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['my_data'], None)

    def test_settings(self):
        client = Client()
        response = client.get('/')
        self.failIfEqual(response.context['settings'], None)

    def test_mydata_form(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/mydata/edit/')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['my_data_form'], None)

    def test_mydata_ajax_form(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/ajax/mydata/edit/')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['my_data_form'], None)

    def test_list_view(self):
        client = Client()
        response = client.get('/httplist/')
        self.failUnlessEqual(response.status_code, 200)
        ht_list = response.context['httplist']
        self.failIfEqual(ht_list, None)
        self.failUnlessEqual(len(ht_list), 10)
        for ht in ht_list:
            self.failIf(ht.id>10, "id lt 10")

    def test_http_save(self):
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

    def test_command(self):
        cmd = 'manage.py printlist'
        if sys.platform == "win32":
            cmd = 'python manage.py printlist' 
        fin, fout, ferr = os.popen3(cmd)
        result = fout.read()
        err = ferr.read()
        self.failUnlessEqual(err, "", "Command not runing!")
        self.failIfEqual(result, "")


