from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def dashboard(request):
    return render(request,"dashboard/dashboard.html")