from django.db import models

class SignIn(models.Model):

    Username = models.CharField(max_length=100, unique = True)
    Password = models.CharField( max_length = 50)
