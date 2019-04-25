from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request,"homepage/index.html")

# def searchjob(request): #search bar processing
#     in_key = re.split('; |, |\*| |,',request.GET['searchbox']) #in_key = [avocado,bean,penut]
#     #put in a list without duplicate
#     newlist = list(set(in_key))