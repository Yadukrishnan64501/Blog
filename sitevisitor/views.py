from django.shortcuts import render,redirect
from userpanel.models import Blog
from.forms import Registration_Form,Login_Form
from django.contrib import messages 
from django.contrib.auth import authenticate,login



# Create your views here.
def sitebase (request):
    blogs=Blog.objects.all().order_by('-id')
    
    
    return render(request,'sitevisitor/site_home.html',{'blogs':blogs})
def registration(request):
    if request.method =='POST':
        form= Registration_Form(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request,'REGISTRATION COMPLETED')
           return redirect('sitevisitor:user_login')
    else:
       form= Registration_Form()
    context={
        'form':form
    }
    return render(request,'sitevisitor/registration.html',context)
def forgot_password(request):
    return render(request,'sitevisitor/forgot_password.html')
def user_login(request):
    if request.method  == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('userpanel:add_blog')
                else:
                    return redirect('userpanel:userbase')
    else:
        form = Login_Form()
    context ={
        'form':form
    }
    return render(request,'sitevisitor/login.html',context)  


def otp(request):
    return render(request,'sitevisitor/otp.html')
def reset_password(request):
    return render(request,'sitevisitor/reset_password.html')    