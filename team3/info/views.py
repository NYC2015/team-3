from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'info/index.html')

def facts(request):
	return render(request, 'info/facts.html')

def resources(request):
	return render(request, 'info/resources.html')