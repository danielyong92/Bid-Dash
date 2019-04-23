from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from django.contrib.auth import login, authenticate
from mysqlconnection import connectToMySQL

def index(request):
    return render(request, "log_reg/login.html")

def signup(request):
    return render(request, "log_reg/signup.html")

def regacc(request):
    mysql = connectToMySQL('bid_dash')
    query = 'INSERT INTO `bid_dash`.`users` (`email`, `password`, `first_name`, `last_name`) VALUES (%(email)s, %(password)s, %(first_name)s, %(last_name)s);'
    pword = request.POST['reg-pw']
    hashed = bcrypt.hashpw(pword.encode(), bcrypt.gensalt())

    data = {
        'email': request.POST['reg-email'],
        'password': hashed.decode(),
        'first_name': request.POST['firstname'],
        'last_name': request.POST['lastname']
    }

    new_user_id = mysql.query_db(query, data)
    request.session['user_id'] = new_user_id
    request.session['logged'] = True
    print('NEW USER INSERTED')
    print('New User ID: ', new_user_id)
    return redirect("/dashboard")

def dashboard(request):
    if request.session['logged'] == False:
        return redirect("/")
    elif request.session['logged'] == True:
        mysql = connectToMySQL('bid_dash')
        
        iduser = request.session['user_id']
        content = {
            "user": mysql.query_db("SELECT * FROM users WHERE id=%(iduser)s"),
        }
        
        return render(request, "log_reg/dashboard.html", content)

def logout(request):
    request.session.clear()
    return redirect('/')
