from django.shortcuts import render,redirect
from .forms import ItemForm

# Create your views here.
def index(request):
    raise Exception("Something Went Wrong!!")
    return  render(request,"sessionApp/index.html")

def addItem(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity  =form.cleaned_data['quantity']
            request.session[name] = quantity
            return redirect('/index/')
    return render(request,"sessionApp/add.html",{'form':form})


def displayItems(request):
    return  render(request,"sessionApp/display.html")