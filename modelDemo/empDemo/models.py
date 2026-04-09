from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=20)
    salary = models.FloatField()
    email = models.CharField(max_length=30)
    
