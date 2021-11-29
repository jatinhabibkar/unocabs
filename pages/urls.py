from django.urls import path

from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('rides',views.rides ,name='rides'),
    path('addride',views.addride ,name='addride'),
    path('apply/<int:cabid>',views.apply),
    path('delcab/<int:cabid>',views.delcab),
    path('deluser/<int:cabid>',views.deluser),
    path('changestep/<int:stepno>/cab/<int:cabid>',views.changestep),
]