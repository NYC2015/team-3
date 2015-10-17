from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from login.forms import NavBarForm, RegisterForm
import datetime


def user_login(request):
	#username = request.POST.get('username', False)
	#password = request.POST.get('password', False)
	if request.method == 'POST':
		form = NavBarForm(request.POST)
		username = form.clean_data['username']
		password = form.clean_data['password']
		user = authenticate(username=username, password=password)
		if (user is not None) and form.is_valid():
			if user.is_active:
				login(request, user)
				# Redirect to a success page.'
				return HttpResponseRedirect('user_login.html')
			else:
				
				return HttpResponseRedirect('exp_user/')
	            
		else:
			
			
			return HttpResponseRedirect('exp_user.html')
			#return render(request, request.META.get('HTTP_REFERER'), {'form':form})
	else:

	#	form = NavBarForm()
		return HttpResponseRedirect( 'user_login.html')

def register_user(requests):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		username = form.clean_data['username']
		password = form.clean_data['password']
		email = form.clean_data['email']
		user = User.object.create_user(username, email, password)

		#user.stuff = 'new stuff'
		user.save()
		good_template = loader.get_template('user_login.html')
		return HttpResponseRedirect('good_register.html')
	else:
		form = RegisterForm()
		return render(request, 'endmysuffering', {'form':form})

def registration_page(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = RegisterForm(request.POST)
	# check whether it's valid:
	#if form.is_valid():
	# process the data in form.cleaned_data as required
	# ...
	# redirect to a new URL:
		return HttpResponseRedirect('/communities')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = RegisterForm()

	return render(request, 'registration.html', {'form':form})