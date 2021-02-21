from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created!')
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register'})

@login_required
def profile(request):
	u_form = UserUpdateForm()
	p_form = ProfileUpdateForm()

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'user/profile.html', context)