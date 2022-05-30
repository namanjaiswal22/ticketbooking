from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseNotFound
from .models import *
from django.contrib.auth.models import User , auth
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    eventdata = events_DB.objects.all()
    return render(request,"index.html",{'eventdata':eventdata})

@login_required(login_url='/login')
def eventregister(request):
    if request.method == "POST":
        name = request.POST.get('eventname')
        desc = request.POST.get('eventdesc')
        venue = request.POST.get('eventvenue')
        time = request.POST.get('eventtime')
        price = request.POST.get('eventprice')
        eventdata = events_DB(username=request.user.username,name=name,desc=desc,venue=venue,time=time,price=price)
        eventdata.save()
        message = "sent for verification"
        return redirect('index')
    return render(request,"event_register.html")

def showallevent(request):
    eventdata = events_DB.objects.all()
    return render(request,"index.html",{'eventdata':eventdata})

def showoneevent(request,id):
    oneeventdata = events_DB.objects.get(id=id)
    return render(request,"one_event_show.html",{'oneeventdata':oneeventdata})

def deleteevent(request,id):
    oneeventdata = events_DB.objects.get(id=id)
    oneeventdata.delete()
    return redirect('showallevent')

def login(request):
    if request.method=="POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)

            return redirect("index")
        else:
            err= "Invalid Username or Password"
            return render(request,"login.html",{'err':err})
    else:
        return render(request,"login.html")

    return render(request.html,"login.html")

def register(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        fullname = request.POST.get('fullname','')
 
        if User.objects.filter(username=username).exists():
            err = "Username Taken"
            return render(request,"register.html",{'err':err})

        else:
            user_main = User.objects.create_user(username=username,password=password,first_name=fullname)
            user_main.save()
            return redirect("login")
    return render(request,"register.html")  

def logout(request):
    auth.logout(request)
    return redirect("/")  

@login_required(login_url='/login')
def book(request,id):
    event = events_DB.objects.get(id=id)
    if request.method=="POST":
        number = request.POST.get('number')
        price = int(event.price)*int(number)
        tprice = price
        book = booked_DB(username=request.user.username,event_name=event.name,number=number,tprice=tprice)
        book.save()
        return redirect('bookedevent')
    return render(request,"book.html",{'event':event})

@login_required(login_url='/login')
def bookedevent(request):
    event = booked_DB.objects.filter(username=request.user.username)
    return render(request,"booked.html",{'event':event})

@login_required(login_url='/login')
def createdevent(request):
    event=events_DB.objects.filter(username=request.user.username)
    return render(request,"created_event.html",{'event':event})
    

