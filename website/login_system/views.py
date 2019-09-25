from django.shortcuts import render
from django.http import HttpResponse
from .helper import *

def login(request):
	context = {
		'error' : None,
		'username' : None,
		'user_id' : None
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		error = None
		if user_exists(username):
			if valid_credentials(username, password):
				error = 'Success'
			else:
				error = 'Invalid password'
		else:
			error = 'Invalid username'
		context['error'] = error
		return render(request, 'user.html', context)
	return render(request, 'login.html', context)

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		return HttpResponse('username {0} password {1}'.format(username, password))
	return render(request, 'register.html')

def user(request):
	return HttpResponse('User')