from django.shortcuts import render
from django.http import HttpResponse

def login(request):
	return HttpResponse('Login')

def register(request):
	return HttpResponse('Register')

def user(request):
	return HttpResponse('User')