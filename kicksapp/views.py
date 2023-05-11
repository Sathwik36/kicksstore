from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate
from kicksapp.models import feedback1
# Create your views here.
def login(request):
    return render(request,'login.html')
    
def verify(request):
   if request.method=="POST":
        username=request.POST.get('username')
        passs=request.POST.get('passs')
        user = authenticate(username=username, password=passs)
        if user is not None:
             # A backend authenticated the credentials
            return render(request,'home.html')
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def deals(request):
    return render(request,'deals.html')

def new(request):
    return render(request,'new.html')
        
def feedback(request):
    return render(request,'feedback.html')

# def submit(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         phone=request.POST.get('phone')
#         email=request.POST.get('email')
#         desc=request.POST.get('desc')
#         fb=feedback()
#         fb.name=name
#         fb.phone=phone
#         fb.email=email
#         fb.desc=desc
#         fb.save()

#     return render(request,'feedback.html')

def submit(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        cont=feedback1()
        cont.name=name
        cont.phone=phone
        cont.email=email
        cont.desc=desc
        cont.save()
    return render(request,'feedback.html')

def buy(request):
    return render(request,'delivery.html')