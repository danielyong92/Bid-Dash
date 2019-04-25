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

        mysql = connectToMySQL('bid_dash')
        jobs = mysql.query_db('SELECT j.*, a.city, u.first_name, u.last_name FROM jobs j JOIN addresses a ON j.addresses_id = a.id JOIN users u ON j.users_id = u.id ORDER BY j.end_datetime;', data)

        content = {
            "user": user,
            "first_name": user[0]["first_name"],
            "last_name": user[0]["last_name"],
            "jobs": jobs
        }
    return render(request, "dashboard/dashboard.html", content)