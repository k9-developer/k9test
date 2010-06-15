# coding: utf-8
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

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
        
    
#    def test_login(self):
#        client = Client()
#        client.login(username='admin', password='admin')
#        response = client.get('/mydata/edit/')
#        self.failUnlessEqual(response.status_code, 200)
