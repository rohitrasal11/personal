from django.shortcuts import render, HttpResponse 
from datetime import datetime
from home.models import Contact 

def index(request):
    context = {
        "variable":"This is Rohit"
    }
    return  render(request,"index.html",context)

    #   return HttpResponse("This is Homepage")

def about(request):
    return  render(request,"about.html")

    # return HttpResponse("This is about page")

def services(request):
    return  render(request,"services.html")

    # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print("reqqqq",request.POST)
        contact = Contact(name=name, email=email, contact=phone,desc=desc, date=datetime.today())
        contact.save()

    return  render(request,"contact.html")


    # return HttpResponse("This is contact page")
