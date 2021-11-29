from django.contrib import admin
from .models import Ride


class RideAdmin(admin.ModelAdmin):
  list_display = ('id','rider', 'name', 'customerId', 'email', 'cost','vehicle','sourName','destName','step1','step2','step3','Rdate','Rtime')
  list_display_links = ('rider','name','email','customerId')
  list_editable = ('step1','step2','step3')
  list_per_page = 25

admin.site.register(Ride, RideAdmin)
