from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from mysqlconnection import connectToMySQL


def dashboard(request):
    if request.session['logged'] == False:
        return redirect("/")
    elif request.session['logged'] == True:
        mysql = connectToMySQL('bid_dash')
        query = "SELECT * FROM users WHERE id=%(iduser)s;"
        data = {
        'iduser': request.session['user_id']
        }
        user = mysql.query_db(query, data)
        # print("First",user[0]["first_name"])
        # print("Last",user[0]["last_name"])
        # print(user)
        content = {
            "user": user,
            "first_name": user[0]["first_name"],
            "last_name": user[0]["last_name"]
        }
    return render(request, "dashboard/dashboard.html", content)