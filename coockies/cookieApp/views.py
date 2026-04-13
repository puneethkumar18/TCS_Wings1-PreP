from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm
import json

# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse("Welcome Home")

def page2(request):
    if request.session.test_cookie_worked():
        print("Cookies are enabled!!")
        request.session.delete_test_cookie()
        return HttpResponse("Cookie worked and deleted!")

    return HttpResponse("This Is Second Page")

def countView(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])+1
    else:
        count = 1
    response = render(request,'cookieApp/count.html',{'count':count})
    response.set_cookie('count',count)
    return response



def index(request):
    return render(request,'cookieApp/index.html')


def addItem(request):
    # 1. Initialize or Load products from Cookie
    if 'products' in request.COOKIES:
        try:
            products = json.loads(request.COOKIES['products'])
        except json.JSONDecodeError:
            products = {} # Fallback if cookie is corrupt
    else:
        products = {}

    # 2. Handle Form Submission
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data['name'])
            quantity = int(form.cleaned_data['quantity'])
            products[name] = quantity
            
            # Create response and set cookie
            response = render(request, 'cookieApp/addItem.html', {
                'form': ItemForm(), # Clear form after success
                'products': products # Pass products to template
            })
            response.set_cookie('products', json.dumps(products), max_age=120)
            return response
    else:
        form = ItemForm()

    # 3. Initial GET request
    return render(request, 'cookieApp/addItem.html', {
        'form': form, 
        'products': products
    })



def displayItems(request):
    # 1. Safely get the cookie. Default to an empty JSON dict '{}'
    products_raw = request.COOKIES.get('products', '{}')
    
    try:
        # 2. Parse the JSON
        products = json.loads(products_raw)
    except json.JSONDecodeError:
        # 3. Fallback if the cookie is malformed
        products = {}

    return render(request, 'cookieApp/displayItem.html', {"products": products})
