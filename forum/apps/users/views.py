from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout	


def log_in(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			errors = True
			return render(request, 'users/login.html', {'errors': errors})
	
	context = {}

	return render(request, 'users/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('/')


def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			fixed_first_name = first_name.replace(" ", "")
			fixed_last_name = last_name.replace(" ", "")

			if fixed_first_name == '':
				form.add_error('first_name', 'First name is required field.')

			if len(fixed_first_name) == 1:
				form.add_error('first_name', 'First name is too short.')

			for char in fixed_first_name:
				if char.isdigit():
					form.add_error('first_name', 'First name contains digits.')
					break

			if fixed_last_name == '':
				form.add_error('last_name', 'Last name is required field.')

			if len(fixed_last_name) == 1:
				form.add_error('last_name', 'Last name is too short.')

			for char in fixed_last_name:
				if char.isdigit():
					form.add_error('last_name', 'Last name contains digits.')
					break

		if form.is_valid():
			user = form.save()
			return render(request, 'users/successfull_reg.html', {'user': user})

	return render(request, 'users/register.html', {'form': form})
