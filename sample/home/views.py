from django.shortcuts import redirect, render, HttpResponse 
from datetime import datetime
from home.models import Contact 
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

# @login_required()
def index(request):
    context = {
        "variable":"This is Rohit"
    }
    return  render(request,"index.html",context)

    #   return HttpResponse("This is Homepage")

# @login_required()
def about(request):
    return  render(request,"about.html")

    # return HttpResponse("This is about page")

# @login_required()
def services(request):
    return  render(request,"services.html")

    # return HttpResponse("This is services page")

# @login_required()
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print("reqqqq",request.POST)
        contact = Contact(name=name, email=email, contact=phone,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent.')


    return  render(request,"contact.html")


    # return HttpResponse("This is contact page")
def loginuser(request):
    if request.method == "POST":
        username= request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/index")
        else:
            return render(request, 'login.html')
            # No backend authenticatedthe credentials

    return render(request, 'login.html')

def logoutuser(request):
    html_template = 'dashboard/login.html'
    logout(request)
    return redirect("/login")