from django import forms

class AskForm(forms.Form):
	question = forms.CharField(label='Question', max_length=500)
	question.widget.attrs.update({'class' : 'form-control'})
	email = forms.CharField(label='Email', max_length=100)
	email.widget.attrs.update({'class' : 'form-control'})
	phone_number = forms.CharField(label='Phone #', max_length=20)  
	phone_number.widget.attrs.update({'class' : 'form-control'})
	location = forms.CharField(label='Location', max_length=100)
	location.widget.attrs.update({'class' : 'form-control'})