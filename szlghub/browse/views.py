from django.shortcuts import render
from django.http import	HttpResponse

def home(request):
	context = {"t":"Browse"}
	return render(request, 'browse.html', context)
