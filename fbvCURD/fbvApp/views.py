from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required
def getStudents(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request,'fbvApp/index.html',context)


@login_required
def home(request):
    return render(request,"fbvApp/home.html")


@login_required
def createStudent(request):
    studentForm = StudentForm()
    if request.method == 'POST':
        studentForm  = StudentForm(request.POST)
        if studentForm.is_valid():
            print("Yest Ist is")
            studentForm.save()
        return redirect('/fbv/')
    return render(request,"fbvApp/createStudent.html",{'studentForm':studentForm})



@login_required
def deleteStudent(request,id):
    student = Student.objects.get(id=id)
    if student:
        student.delete()
    else:
        raise ModuleNotFoundError("NOt Found")
    return redirect('/fbv/')


def logoutUser(request):
    logout(request)
    return redirect('/fbv/')

@login_required
def updateStudent(request,id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        studentForm = StudentForm(request.POST,instance=student)
        if studentForm.is_valid():
            studentForm.save()
            return redirect('/fbv/')
    return render(request,"fbvApp/update.html",{'student':student})