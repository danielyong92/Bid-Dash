from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import re
from mysqlconnection import connectToMySQL
import operator

from django.db.models import Q

def index(request):
    return render(request,"homepage/index.html")

# def searchjob(request): #search bar processing
#     in_key = re.split('; |, |\*| |,',request.GET['searchbox']) #in_key = [avocado,bean,penut]
#     #put in a list without duplicate
#     newlist = list(set(in_key))
#     if len(newlist) == 1:
#         try:
#             #ingre_input = Jobs.objects.get(title=str(in_key[0]).lower())
#             finalarray = Jobs.objects.filter(title=str(in_key[0]).lower())
#             if not finalarray:
#                 return render(request, "dashboard/notfound.html")
#             else:
#                 context = {
#                     "found": len(finalarray),
#                     "recipes": finalarray
#                 }
#         except Jobs.DoesNotExist:
#             return render(request, "dashboard/jobdoesnotexits.html")
#     else:
#         query_set_array = []
#         for i in newlist:
#             try:
#                 #ingre_input = Ingre.objects.get(ingre_name=str(i).lower())
#                 a = Jobs.objects.filter(title=str(i).lower())
#                 query_set_array.extend(a)
#             except Jobs.DoesNotExist:
#                 pass
#         finalarray = list(set(query_set_array))
#         if not finalarray:
#             return render(request, "dashboard/notfound.html")
#         else:
#             context = {
#                 "found": len(finalarray),
#                 "recipes": finalarray
#             }
#     return render(request, "dashboard/recipeslist.html", context)

# def search(request):
#     if request.method == 'GET': 
#         in_key = re.split('; |, |\*| |,',request.GET['searchbox']) #in_key = [avocado,bean,peanut]
#         #put in a list without duplicate
#         newlist = list(set(in_key))
#         final_array = []
#         for i in newlist:
#             mysql = connectToMySQL('bid_dash')
#             query = "SELECT * FROM jobs WHERE title LIKE '%(searchbox)s' AND category_id = 1;"
#             data = {
#                 'searchbox': i
#                 }
#             result = mysql.query_db(query, data)
#             final_array += result
#         print("///////////////////////////////////////////////")
#         print(final_array)
#         content= {
#             "jobs": final_array
#         }
#         return render(request,"dashboard/dashboard.html", content)
#     else:
#         return redirect("/dashboard")

def onlinejob(request):
    mysql = connectToMySQL('bid_dash')
    query = "SELECT * FROM jobs WHERE category_id = 1;"
    result = mysql.query_db(query)
    context = {
        "jobs": result
    }
    return render(request,"dashboard/dashboard.html", context)

def automotive(request):
    mysql = connectToMySQL('bid_dash')
    query = "SELECT * FROM jobs WHERE category_id = 2;"
    result = mysql.query_db(query)
    context = {
        "jobs": result
    }
    return render(request,"dashboard/dashboard.html", context)

def house(request):
    mysql = connectToMySQL('bid_dash')
    query = "SELECT * FROM jobs WHERE category_id = 3;"
    result = mysql.query_db(query)
    context = {
        "jobs": result
    }
    return render(request,"dashboard/dashboard.html", context)

def pets(request):
    mysql = connectToMySQL('bid_dash')
    query = "SELECT * FROM jobs WHERE category_id = 4;"
    result = mysql.query_db(query)
    context = {
        "jobs": result
    }
    return render(request,"dashboard/dashboard.html", context)

def photography(request):
    mysql = connectToMySQL('bid_dash')
    query = "SELECT * FROM jobs WHERE category_id = 5;"
    result = mysql.query_db(query)
    context = {
        "jobs": result
    }
    return render(request,"dashboard/dashboard.html", context)

def misc(request):
    mysql = connectToMySQL('bid_dash')
    query = "SELECT * FROM jobs WHERE category_id = 6;"
    result = mysql.query_db(query)
    context = {
        "jobs": result
    }
    return render(request,"dashboard/dashboard.html", context)