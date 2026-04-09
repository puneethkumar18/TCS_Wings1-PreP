from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.
def userRegistration(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST':
        print("Yes We Got Post Request!!!")
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['firstName'])
            print(form.cleaned_data['lastName'])
    context = {'form': form}
    return  render(request,'formsApp/register.html',context=context)
