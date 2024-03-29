from django.shortcuts import render
from django.http import HttpResponseRedirect
from ask.forms import AskForm

# Create your views here.
def index(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('submitted/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AskForm()
	
	return render(request, 'ask/ask.html', {'form':form})

def submitted(request):
	return render(request, 'ask/thanks.html')