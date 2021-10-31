from django.shortcuts import render

# Create your views here.


def login(request):

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email =request.POST['email']
        password = request.POST['password']


        print(username,email,password)
        return render(request,'accounts/login.html')
    return render(request,'accounts/register.html')