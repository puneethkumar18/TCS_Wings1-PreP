from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,"templateApp/index.html")


def renderData(request):
    context = [
        "Tiger",
        "Lion",
        "cheetha",
        "Elephat"
    ]
    return render(request,"templateApp/home.html",context={"data":context})


def elctronics(request):
    dictionary = {
        "product1":"Fan",
        "product2":"Mixy",
        "product3":"Grinder"
    }
    return render(request,"templateApp/electronics.html",context=dictionary)