from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    testScore = models.FloatField()


    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
    