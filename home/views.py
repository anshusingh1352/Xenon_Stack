from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
import templates
from django.shortcuts import redirect
from home.models import savedata_model,savedata_contact

# Create your views here.

def home(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user=savedata_model.objects.filter(email=email,password=password).exists()
        if user:
            request.session['email']=email
            session_id=request.session['email']
            print(session_id)
            return render(request,"index.html",{session_id:session_id})
        else:
            return redirect('/')
    return render(request,'signin.html')

def register(request):
    return render(request, 'register.html')

def savedata(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        country = request.POST.get('country')
        en=savedata_model(first_name=first_name,last_name=last_name,birthday=birthday,email=email,phone=phone,password=password,country=country)
        en.save()
    return render(request,'signin.html')

def savedata_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en=savedata_contact(name=name,email=email,phone=phone,message=message)
        en.save()
    return render(request,'Contact.html')

def dashboard(request):
    if request.session.has_key('email'):
        return render(request,'index.html')
    else:
        return render(request,'signin.html')

def logout_fun(request):
    del request.session['email']
    print("Session Closed")
    return render(request,'signin.html')

def about(request):
    if request.session.has_key('email'):
        return render(request,'about.html')
    else:
        return render(request,'signin.html')

def computer(request):
    if request.session.has_key('email'):
        return render(request,'computer.html')
    else:
        return render(request,'signin.html')

def Contact(request):
    if request.session.has_key('email'):
        return render(request,'Contact.html')
    else:
        return render(request,'signin.html')


def laptop(request):
    if request.session.has_key('email'):
        return render(request,'laptop.html')
    else:
        return render(request,'signin.html')

def product(request):
    if request.session.has_key('email'):
        return render(request,'product.html')
    else:
        return render(request,'signin.html')