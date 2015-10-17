from django import forms

class NavBarForm(forms.Form):
	username = forms.CharField(label = "username", max_length=30)
	password = forms.CharField(label = "password", max_lenth=30)