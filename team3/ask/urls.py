"""
ask.urls.py
"""
from django.conf.urls import include, url
from django.contrib import admin
from ask import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^submitted', views.submitted, name='submitted')
]