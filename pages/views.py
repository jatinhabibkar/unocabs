from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def rides(request):
    return render(request,'pages/rides.html')

def addride(request):
    if request.method == 'POST':
        cost = request.POST['cost']
        message = request.POST['message']
        datetime = request.POST['datetime']
        location1= request.POST['location1']
        location2= request.POST['location2']
        


        print(cost,message,datetime,location1,location2)
    return render(request,'pages/addride.html')
