from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.core.serializers import serialize
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime
import json
from .models import Ride
from django.utils.html import escape


# Create your views here.
def index(request):
    rides = Ride.objects.all()
    rides= serialize('json',rides)
    context={
        "rides":rides
    }
    return render(request,'pages/index.html',context)

def rides(request):
    return render(request,'pages/rides.html')

def addride(request):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            
            email = request.user.username
            name = request.user.first_name
            cost = request.POST['cost']
            message = request.POST['message']
            tel=request.POST['tel']
            vehicle = request.POST['vehicle']
            location1= request.POST['location1'].split(',')
            locationname1 = request.POST['locationname1']
            locationname2 = request.POST['locationname2']
            location2= request.POST['location2'].split(',')
            mydate= request.POST['datetime']
            mytime =request.POST['time']  
            ride = Ride(
                rider=request.user,
                name=name,email=email,tel=tel,cost=int(cost),message=message,vehicle=vehicle,
                sourName=locationname1,Scordlog=float(location1[0]),Scordlat=float(location1[1]),
                destName=locationname2,Dcordlog=float(location2[0]),Dcordlat=float(location2[1]),
                Rdate = datetime.strptime(mydate, '%d/%m/%Y'),
                Rtime = datetime.strptime(mytime, '%I:%M %p')
            )

            ride.save()
            messages.success(request, 'Your request has been submitted')
        except Exception as e:
            print(e)
            messages.error(request,'something went wrong')
        return redirect('addride')

    return render(request,'pages/addride.html')


def apply(request,userid=None):
    if(userid == None):
        messages.error(request,'something went wrong')    
        return redirect("")
    if(request.user.id and userid == request.user.id):
        messages.error(request,'you cannot apply to your own cab service')
        return redirect('rides')
    else:
        data = Ride.objects.get(pk=userid)
        print(data)
        messages.success(request,'you applied to '+data.name +'cab service')
        return redirect('rides')



