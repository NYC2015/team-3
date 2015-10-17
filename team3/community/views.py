from django.shortcuts import render
from community.forms import CommunityCreationForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'community/index.html')

def create(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = CommunityCreationForm(request.POST)
	# check whether it's valid:
		if form.is_valid():
	# process the data in form.cleaned_data as required
	# ...
	# redirect to a new URL:
			return HttpResponseRedirect('/communities')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = CommunityCreationForm()

	return render(request, 'community/makecommunities.html', {'form':form})

def community1(request):
	return render(request, 'community/comm1.html')