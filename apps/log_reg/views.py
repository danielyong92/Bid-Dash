from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from django.contrib.auth import login, authenticate
from mysqlconnection import connectToMySQL

def login(request):
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

# def dashboard(request):
#     if request.session['logged'] == False:
#         return redirect("/")
#     elif request.session['logged'] == True:
#         mysql = connectToMySQL('bid_dash')
#         query = "SELECT * FROM users WHERE id=%(iduser)s;"
#         data = {
#         'iduser': request.session['user_id']
#         }
#         user = mysql.query_db(query, data)
#         # print("First",user[0]["first_name"])
#         # print("Last",user[0]["last_name"])
#         # print(user)
#         content = {
#             "user": user,
#             "first_name": user[0]["first_name"],
#             "last_name": user[0]["last_name"]
#         }
#     return render(request, "log_reg/dashboard.html", content)

def logout(request):
    request.session.clear()
    return redirect('/')

def logacc(request):
    mysql = connectToMySQL('bid_dash')
    # thisuser = mysql.query_db("SELECT * FROM users WHERE email=%(email)s;")
    query = "SELECT * FROM users WHERE email=%(email)s;"
    data = {
        'email': request.POST['log-email']
        }
    user = mysql.query_db(query, data)
    request.session['user_id'] = user[0]["id"]
    print('////////////////////////////////////////')
    print(request.session['user_id'])
    if (len(user) < 1):
        return redirect("/")
    else:
        if not bcrypt.checkpw(request.POST['log-pw'].encode(), user[0]["password"].encode()):
            return redirect("/")
        else:
            content = {
                "user" : user,
                "first_name": user[0]["first_name"],
                "last_name": user[0]["last_name"]
                }
            request.session['logged'] = True
            return redirect('/dashboard')