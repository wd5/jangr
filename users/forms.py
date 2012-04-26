# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=50,label="Име")
	password = forms.CharField(max_length=50,widget=forms.PasswordInput,label="Парола")
	remember_me = forms.BooleanField(label="Запомни ме")
	pass
 
class RegistrationForm(UserCreationForm	):
	username = forms.CharField(max_length=50,label="Име")
	password1 = forms.CharField(max_length=50,widget=forms.PasswordInput,label="Парола")
	password2 = forms.CharField(max_length=50,widget=forms.PasswordInput,label="Парола (пак същата)")
	email = forms.EmailField(label="Мейл")
	
	def clean_password1(self):
		if self.data['password1'] != self.data['password2']:
			raise forms.ValidationError('Passwords are not the same')
		return self.data['password1']
    
	def clean(self, *args, **kwargs):
		self.clean_password1()
		return super(UserCreationForm, self).clean(*args, **kwargs)