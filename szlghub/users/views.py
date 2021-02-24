from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
import random

#register page
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created!')
			return redirect('/login')
	else:
		form = UserCreationForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register'})

#edit profile data (user+profile)
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Account updated!')
			return redirect('/profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'user/profile.html', context)

#about page init
def about(request):
	return render(request, 'user/about.html')

#about page init + get random user
def browse(request):
	context = {
		'Profile':Profile.objects.order_by("?").first()
	}
	return render(request, 'user/browse.html', context)

#about page init + get all users
def table(request):
	context = {
		'Profile':Profile.objects.all()
	}
	return render(request, 'user/table.html', context)