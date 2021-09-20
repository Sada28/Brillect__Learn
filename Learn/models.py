from django.db import models

class Newuser(models.Model):
    fullname=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    pwwd=models.CharField(max_length=150)
    
    