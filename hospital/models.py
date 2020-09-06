from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    realname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    status = models.BooleanField()
    role = models.CharField(max_length=10)

class ChargeManag(models.Model):
    aname = models.CharField(max_length=50)
    pname = models.CharField(max_length=10)



