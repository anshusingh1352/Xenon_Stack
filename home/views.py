from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
import templates
from django.shortcuts import redirect

# Create your views here.
emailid=""

def home(request):
    return render(request,'signin.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            birthday = form.cleaned_data.get('birthday')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            print(first_name,last_name,birthday,email,phone)
            user = authenticate(first_name=first_name, last_name=last_name,birthday=birthday,email=email,phone=phone)
            login(request, user)
            print("Code working")
            return redirect('dashboard')
        else:
            return render(request, 'register.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html')
   
def home(request): 
    return render(request, 'home.html')
    return render(request,'register.html')
    
def dashboard(request):
    return render(request,'index.html')

def logout_fun(request):
    return_data=delete_session(request)
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def computer(request):
    return render(request,'computer.html')

def Contact(request):
    return render(request,'Contact.html')

def laptop(request):
    return render(request,'laptop.html')

def product(request):
    return render(request,'product.html')