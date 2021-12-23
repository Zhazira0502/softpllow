from django.shortcuts import render,redirect
from .models import *
from django.contrib.messages.api import error
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib import messages

def index(request):
    service1=Service.objects.all()
    staff=Staff.objects.all()
    return render(request,'index.html',{'service1':service1,'staff':staff})
def about(request):
    staff=Staff.objects.all()
    return render(request,'about.html',{'staff':staff})

def service(request):
    service1=Service.objects.all()
    return render(request,'services.html',{'service1':service1})
def sale(request):
    service1=Service.objects.all()
    return render(request,'sales.html',{'service1':service1})
def contacts(request):
    return render(request,'contact.html',{})

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.error(request,error)
    else:
        form=UserCreationForm()
    return render(request,'registration.html',{'form':form})

def zapis(request,pk):
    service=Service.objects.get(pk=pk)
    rec=Record.objects.filter(service=service)
    return render(request,'zapis.html',{'service':service,'rec':rec})

def userlogin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,error)
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})
def userlogout(request):
    logout(request)
    return redirect('index')
    
def person(request,pk):
    rec=Record.objects.get(pk=pk)
    return render(request,'order.html',{'rec':rec})

def order(request,pk):
    
    rec = Record.objects.get(pk=pk)
    person = Person.objects.create(name=request.GET.get('fname'),phone=request.GET.get('number'))
    rec.customer=person
    person.save()
    rec.save()
    return redirect('index')
    