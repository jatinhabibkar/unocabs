from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(password=password ,username=email)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"user login")
            return redirect('login')
        else:
            messages.error(request,"wrong credentials")
            return redirect('login')

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        password2= request.POST['password2']
        if(password == password2):
            if User.objects.filter(email=email).exists():
                messages.error(request,'this email already taken')
                return redirect('register')
            else:  
                user=User.objects.create_user(username=email,password=password,email=email,first_name=username)
                user.save()
                auth.login(request,user)
                messages.success(request,'User created')
                return redirect('login')
        else:
            messages.error(request, 'password not same')
            return redirect('register')

    return render(request,'accounts/register.html')