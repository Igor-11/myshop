from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, null= True, blank=True)
    email = models.EmailField(max_length=150, null= True, blank=True)
    password = models.CharField(max_length=50, null= True, blank=True)

