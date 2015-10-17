from django import forms

class NavBarForm(forms.Form):
	username = forms.CharField(widget = forms.Textarea(), label = "username", max_length=30)
	username.widget.attrs.update({'class' : 'form-control'})
	password = forms.CharField(widget = forms.Textarea(), label = "password", max_length=30)
	password.widget.attrs.update({'class' : 'form-control'})

class RegisterForm(forms.Form):
	username = forms.CharField(label = "username", max_length=30)
	username.widget.attrs.update({'class' : 'form-control'})
	password = forms.CharField(label = "password", max_length=30)
	password.widget.attrs.update({'class' : 'form-control'})
	first_name = forms.CharField(label = "firstname", max_length=30)
	first_name.widget.attrs.update({'class' : 'form-control'})
	last_name = forms.CharField(label = "lastname", max_length=30)
	last_name.widget.attrs.update({'class' : 'form-control'})
	location = forms.CharField(label = "location", max_length=30)
	location.widget.attrs.update({'class' : 'form-control'})
	age = forms.CharField(label = "age", max_length=30)
	age.widget.attrs.update({'class' : 'form-control'})