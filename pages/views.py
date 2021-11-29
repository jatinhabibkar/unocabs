from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime
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
    # step one
    if request.method == 'POST' and request.user.is_authenticated:
        cabid = request.POST['cabid']
        
        ride = Ride.objects.get(id = cabid)
        if(ride.customerId ==-1):
            customerid = request.POST['customerid']
        
        userid = ride.rider.id 
        if(userid == request.user.id and str(customerid) in ride.applied.split(",")[:-1]):
            if(not ride.step1):
                cos =User.objects.get(id=customerid)
                Ride.objects.filter(id = cabid).update(step1=True,customerId=customerid)
                messages.success(request,"message will we send to "+ cos.first_name)
                return redirect('rides')
            else:
                messages.error(request,'something went wrong')
                return redirect('rides')
        return redirect('rides')
    
    allrides = Ride.objects.all()
    myrides = []
    applied_ride = []
    applied_count=[]
    users = []
    for consumer in allrides.iterator():
        if consumer.rider.id == request.user.id:
            myrides.append(consumer)
            user=[]
            allconsumer = consumer.applied.split(",")[:-1]
            for i in allconsumer:
                user.append(User.objects.get(id=i))
            users.append(user)
        
        if str(request.user.id) in consumer.applied.split(",")[:-1]:
            applied_ride.append(consumer)
            applied_count.append(len(consumer.applied.split(",")[:-1]))
    applied_data = zip(applied_ride,applied_count)
    mydata = zip(myrides,users)
    context ={
        'mydata':mydata,
        'applied_data':applied_data,
        'render': True if len(myrides)>0 else False,
        'render0':True if len(applied_count)>0 else False

    }
    
    return render(request,'pages/rides.html',context)

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


def apply(request,cabid=None):

    if(not request.user.is_authenticated or cabid == None):
        messages.error(request,'login first')    
        return redirect("login")
    ride =  Ride.objects.get(id=cabid)
    userid =ride.rider.id
    if(request.user.id and userid == request.user.id):
        messages.error(request,'you cannot apply to your own cab service')
        return redirect('rides')
    elif(request.user.id and userid != request.user.id):
        currentride = ride
        listofapplied=''
        if(currentride.applied is None):
            listofapplied =str(request.user.id)+','
        elif(str(request.user.id) in currentride.applied.split(",")[:-1]):
            messages.error(request,"Sorry you can't again applied to "+currentride.name +" cab service")
            return redirect('rides')
        else:
            listofapplied = currentride.applied + str(request.user.id) +','
            Ride.objects.filter(id=cabid).update(applied=listofapplied)
        messages.success(request,'you applied to '+currentride.name +' cab service')
        return redirect('rides')
    else:
        messages.error(request,'login first')
        return redirect('rides')





def delcab(request,cabid=None):
    if(not request.user.is_authenticated or cabid == None):
        messages.error(request,'login first')    
        return redirect("login")
    ride =  Ride.objects.get(id=cabid)
    userid =ride.rider.id
    if(userid == request.user.id):
        Ride.objects.filter(id=cabid).delete()
        messages.success(request,'ride deleted')  
        return redirect('rides')
    return redirect('login')

def deluser(request,cabid=None):
    if(not request.user.is_authenticated or cabid == None):
        messages.error(request,'login first')    
        return redirect("login")
    ride =  Ride.objects.get(id=cabid)
    customerid= str(request.user.id)
    allconsumer = ride.applied.split(",")[:-1]
    if(customerid in allconsumer):
        var = ride.applied.replace(f"{customerid},",'')
        Ride.objects.filter(id=cabid).update(applied = var)
        messages.success(request,'u optted out from the service')
        return redirect('rides')
    else:
        messages.error(request,'something went wrong')
        return redirect('rides')


def changestep(request,stepno=None,cabid=None):
    if(not request.user.is_authenticated or cabid == None):
        messages.error(request,'login first')    
        return redirect("login")
    ride =  Ride.objects.get(id=cabid)
    if(stepno == 2 and ride.customerId == request.user.id and ride.step1):
        Ride.objects.filter(id = cabid).update(step2=True,customerId=ride.customerId)
    if(stepno == 3 and ride.rider.id == request.user.id and ride.step1 and ride.step2):
        Ride.objects.filter(id = cabid).update(step3=True,customerId=ride.customerId)
    return redirect('rides')