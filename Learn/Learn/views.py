from django.http import request
from django.shortcuts import render
from Learn.models import Newuser
from django.contrib import messages
def Indexpage(request):
    return render(request,'index.html')
def dashpage(request):
    return render(request,'dashboard.html')

def userreg(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        Email=request.POST['Email']
        pwwd=request.POST['pwwd']
       

        Newuser(fullname=fullname,username=username,Email=Email,pwwd=pwwd).save()
        messages.success(request,'The New user '+request.POST['username']+" Is Saved Sucessfully..!")
        return render(request,'Registration.html')
    else:
        return render(request,'Registration.html')

def loginpage(request): 
    if request.method=="POST":
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'],pwwd=request.POST['pwwd'])
            print("username",Userdetails)
            request.session['Email']=Userdetails.Email
            return render(request,'dashboard.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid..!')
    return render(request,'Login.html')

def pypage(request):
        return render(request,'python.html')

def ml(request):
        return render(request,'ml.html')

def java(request):
        return render(request,'java.html')

def web(request):
        return render(request,'web.html')

def android(request):
        return render(request,'android.html')

def clang(request):
    return render(request,'clang.html')

def cpp(request):
    return render(request,'cpp.html')


