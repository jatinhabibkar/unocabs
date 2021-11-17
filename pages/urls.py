from django.urls import path

from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('rides',views.rides ,name='rides'),
    path('addride',views.addride ,name='addride'),
    path('apply/<int:userid>',views.apply)
]