from django.db import models
from django.core import validators

# Create your models here.

class Project(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField()
    assignedTo = models.CharField(max_length=40)
    priority = models.IntegerField()