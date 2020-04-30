from django.shortcuts import render
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout	

def log_in(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
	return render(request, 'users/login.html', {'form': form})

def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')

			if first_name.replace(" ", "") == '':
				form.add_error('first_name', 'First name is required field.')

			if len(first_name.replace(" ", "")) == 1:
				form.add_error('first_name', 'First name is too short.')

			for char in first_name.replace(" ", ""):
				if char.isdigit():
					form.add_error('first_name', 'First name contains digits.')
					break

			if last_name.replace(" ", "") == '':
				form.add_error('last_name', 'Last name is required field.')

			if len(last_name.replace(" ", "")) == 1:
				form.add_error('last_name', 'Last name is too short.')

			for char in last_name.replace(" ", ""):
				if char.isdigit():
					form.add_error('last_name', 'Last name contains digits.')
					break

		if form.is_valid():
			user = form.save()
			return render(request, 'users/successfull_reg.html', {'user': user})

	return render(request, 'users/register.html', {'form': form})
