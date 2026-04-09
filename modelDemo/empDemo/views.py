from django.shortcuts import render
from .models import Employee

# Create your views here.
def employeedata(request):
    employees = Employee.objects.all()
    dictionary = {"data":employees}
    return render(request,"modelDemo/emptemplate.html",dictionary)