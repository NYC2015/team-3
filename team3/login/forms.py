from django import forms

class NavBarForm(forms.Form):
	username = forms.CharField(label = "username", max_length=30)
	password = forms.CharField(label = "password", max_lenth=30)

class RegisterFrom(forms.Form):
	username = forms.CharField(label = "username", max_length=30)
	password = forms.CharField(label = "password", max_length=30)
	first_name = forms.CharField(label = "firstname", max_length=30)
	last_name = forms.CharField(label = "lastname", max_lenth=30)
	location = forms.CharField(label = "location", max_length=30)
	age = forms.CharField(label = "age", max_length=30)
	