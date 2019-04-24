from django.shortcuts import render, HttpResponse
from mysqlconnection import connectToMySQL
import bcrypt
from .models import *

def profile(request):

    mysql = connectToMySQL('bid_dash')

    data = {'user_id': 1}
    user = mysql.query_db('SELECT * FROM users WHERE id = %(user_id)s;', data)

    # jobs = mysql.query_db('SELECT * FROM jobs WHERE users_id = %(user_id)s ORDER BY end_datetime;', data)
    jobs = mysql.query_db('SELECT * FROM jobs;')

    context = {
        "user": user[0],
        # "jobs": []
    }
    print(user[0])

    return render(request, "users/profile.html", context)