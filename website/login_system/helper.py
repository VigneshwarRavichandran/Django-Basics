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

def create_user(username, password, firstname, lastname):
	user = Users(username=username, password=password)
	user.save()
	user_details = UserDetails(firstname=firstname, lastname=lastname, user_id=user.id)
	user_details.save()

def get_user_details(userid):
	user_details = UserDetails.objects.get(user_id=userid)
	return user_details