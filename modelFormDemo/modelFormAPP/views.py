from django.shortcuts import render
from .forms import ProjectModelForm
from .models import Project
# Create your views here.
def addProject(request):
    form = ProjectModelForm()
    if request.method == 'POST':
        print("Yes , IT is a POST Request.")
        form = ProjectModelForm(request.POST)
        if form.is_valid():
            print("And Also it is valid !!")
            form.save()
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,'modelFormAPP/addProject.html',context)


def listOfProjects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'modelformAPP/listofprojects.html',context)


def index(request):
    return render(request,'modelformAPP/index.html')
