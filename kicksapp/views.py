from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate
from kicksapp.models import feedback1,mailm
from django.core.mail import EmailMessage
from django.conf import settings
import random
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
            # return render(request,'home.html')
            return redirect("/home")
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
    context={
        "c":0
    }
    return render(request,'delivery.html',context)

def mail(request):
    rname=request.POST.get('dname')
    sendermail=request.POST.get('demail')
    otp=random.randint(0000,9999)
    temp='Hello '+rname+'\nYour OTP is : '+str(otp)+'\nDO NOT share with any one'
    email=EmailMessage(
        'OTP for KICKS Order Confirmation',
        temp ,
        settings.EMAIL_HOST_USER,
        [sendermail],
        )
    
    email.fail_silently=False
    email.send()
    
    if request.method=="POST":
        tempobj=mailm()
        tempobj.email=sendermail
        tempobj.otp=otp
        tempobj.addr=request.POST.get('daddress')
        tempobj.save()


    context={
        "c":1
    }
    return render(request,'delivery.html',context)

def otpverify(request):
    if request.method=="POST":
        otpval=request.POST.get('otpval')
        query=mailm.objects.all()[0]
        context={
            "address":query.addr
        }
        if str(otpval)==str(query.otp):
            query.delete()
            return render(request,'delivery.html',context)
        else:
            query.delete()
            return HttpResponse("You entered wrong Otp    Please go back to home  ")