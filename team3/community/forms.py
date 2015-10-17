from django import forms

class CommunityCreationForm(forms.Form):
	name = forms.CharField(label="Name", max_length=100)
	name.widget.attrs.update({'class' : 'form-control'})
	description = forms.CharField(widget=forms.Textarea(), label="description", max_length=500)
	description.widget.attrs.update({'class' : 'form-control'})