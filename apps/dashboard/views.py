from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from mysqlconnection import connectToMySQL


def dashboard(request):
    if 'user_id' not in request.session:
        mysql = connectToMySQL('bid_dash')
        jobs = mysql.query_db('SELECT j.*, a.city, u.first_name, u.last_name FROM jobs j JOIN addresses a ON j.addresses_id = a.id JOIN users u ON j.users_id = u.id ORDER BY j.end_datetime;')
        content = {
            "jobs": jobs
        }
    else:
        mysql = connectToMySQL('bid_dash')
        data = {
        'iduser': request.session['user_id']
        }
        user = mysql.query_db("SELECT * FROM users WHERE id=%(iduser)s;", data)
        # print("First",user[0]["first_name"])
        # print("Last",user[0]["last_name"])
        # print(user)
        mysql = connectToMySQL('bid_dash')
        jobs = mysql.query_db('SELECT j.*, a.city, u.first_name, u.last_name FROM jobs j JOIN addresses a ON j.addresses_id = a.id JOIN users u ON j.users_id = u.id ORDER BY j.end_datetime;')
        content = {
            "user": user,
            "first_name": user[0]["first_name"],
            "last_name": user[0]["last_name"],
            "jobs": jobs
        }
    return render(request, "dashboard/dashboard.html", content)