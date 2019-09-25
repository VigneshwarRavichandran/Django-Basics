from .models import *	

def user_exists(username):
	user = Users.objects.filter(username=username)
	if user:
		return True
	return False

def valid_credentials(username, password):
	user = Users.objects.get(username=username)
	if user.password == password:
		return user
	return False