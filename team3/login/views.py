from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader

import datetime


def user_login(request):
	#username = request.POST.get('username', False)
	#password = request.POST.get('password', False)
	form = NavBarForm(POST.request)
	username = form.username
	password = form.password
	user = authenticate(username=username, password=password)
	good_template = loader.get_template('user_login.html')
	exp_template = loader.get_template('exp_user.html')
	bad_template = loader.get_template('bad_login.html')
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.'
			return HttpResponse(good_template.render())
		else:
			
			return HttpResponse(exp_template.render())
            
	else:
		
		return HttpResponse(bad_template.render())
        # Return an 'invalid login' error message.
        
        
def register_user(requests):
	username = request.POST.get('username', False)
	password = request.POST.get('password', False)
	email = request.POST.get('email', False)
	user = User.object.create_user(username, email, password)

	#user.stuff = 'new stuff'
	user.save()
	good_template = loader.get_template('user_login.html')
	return HttpResponse(good_template.render())

def registration_page(request):
	return render(request, 'registration.html')