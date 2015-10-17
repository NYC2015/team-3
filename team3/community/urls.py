"""
community.urls.py
"""
from django.conf.urls import include, url
from django.contrib import admin
from community import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create', views.create, name='create'),
	url(r'^community1', views.community1, name='community1'),
]