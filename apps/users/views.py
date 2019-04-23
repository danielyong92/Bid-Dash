from django.shortcuts import render, HttpResponse
from mysqlconnection import connectToMySQL
import bcrypt
from .models import *

def profile(request):

    mysql = connectToMySQL('bid_dash')
    query = 'INSERT INTO users (email, password, first_name, last_name) VALUES (%(email)s, %(password)s, %(first_name)s, %(last_name)s);'
    pword = "password"
    hashed = bcrypt.hashpw(pword.encode(), bcrypt.gensalt())

    data = {
        'email': "dy@mail.com",
        'password': hashed.decode(),
        'first_name': "Daniel",
        'last_name': "Yong"
    }

    new_user_id = mysql.query_db(query, data)
    print('NEW USER INSERTED')
    print('New User ID: ', new_user_id)

    return render(request, "users/profile.html")