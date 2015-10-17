"""
info.urls.py
"""
from django.conf.urls import include, url
from django.contrib import admin
from info import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^facts/', views.facts, name='facts'),
	url(r'^resources/', views.resources, name='resources'),
	url(r'^view-profile/', views.profile, name='profile'),
]