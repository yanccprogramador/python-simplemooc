#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import *
from simplemooc.core import views
app_name='core'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contact, name='contact'),
]