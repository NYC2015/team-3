from django.conf.urls import url

from . import views

urlpatterns =[
	url(r'^$', views.user_login, name='user_login'),
	url(r'^$', views.user_login, name='exp_user'),
	url(r'^$', views.user_login, name='bad_login'),
]