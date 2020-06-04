from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta():
		model = User
		fields = ["username", "email", "first_name", "last_name"]
		error_css_class = 'error'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'autofocus': False, 'maxlength': 15})
		self.fields['first_name'].widget.attrs.update({'required': True, 'maxlength': 30})
		self.fields['last_name'].widget.attrs.update({'required': True, 'maxlength': 30})
		self.fields['email'].widget.attrs.update({'required': True, 'maxlength': 50})
		self.fields['password1'].widget.attrs.update({'required': True, 'maxlength': 35})
		self.fields['password2'].widget.attrs.update({'required': True, 'maxlength': 35})
		