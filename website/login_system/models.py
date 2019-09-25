from django.db import models

class Users(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

class UserDetails(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	user = models.ForeignKey(Users, on_delete=models.CASCADE)