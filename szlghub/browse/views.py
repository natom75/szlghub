from django.shortcuts import render
from django.http import	HttpResponse
from ..users.models import Profile

def home(request):
	context = {"title":"Browse"}

	data = Profiles.objects.all()
	prof = {
    "user": data
	}
	return render_to_response('browse.html', prof)