from django.test import TestCase
from django.shortcuts import render

# Create your tests here.

def index(request):
    return render(request,'pages/index.html')