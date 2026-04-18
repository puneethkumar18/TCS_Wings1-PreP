from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=20)
    salary = models.FloatField()
    email = models.CharField(max_length=30)
    



class Programmer(models.Model):
    name = models.CharField(max_length=30)
    salary = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=30)
    programeers = models.ManyToManyField(Programmer)


class Customer(models.Model):
    name = models.CharField(max_length=30)


class PhoneNumbers(models.Model):
    type = models.CharField(max_length=20)
    number = models.CharField(max_length=12)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)



class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class Licence(models.Model):
    type  = models.CharField(max_length=30)
    validfrom =  models.DateField()
    validTo = models.DateField()
    person = models.OneToOneField(Person,on_delete=models.CASCADE)