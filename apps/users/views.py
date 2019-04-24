from django.shortcuts import render, HttpResponse
from mysqlconnection import connectToMySQL
from django.contrib.auth import login, authenticate
import bcrypt

def profile(request):
    if request.session['logged'] == False:
        return redirect("/")
    elif request.session['logged'] == True:
        mysql = connectToMySQL('bid_dash')

        data = {'user_id': request.session['user_id']}
        # data = {'user_id': 1} #for testing the user_id
        user = mysql.query_db('SELECT * FROM users WHERE id = %(user_id)s;', data)

        mysql = connectToMySQL('bid_dash')
        jobs = mysql.query_db('SELECT * FROM jobs WHERE users_id = %(user_id)s ORDER BY end_datetime;', data)

        mysql = connectToMySQL('bid_dash')
        bids = mysql.query_db('SELECT * FROM bids JOIN jobs ON bids.jobs_id = jobs.id WHERE bids.users_id = %(user_id)s ORDER BY jobs.end_datetime;', data)

        context = {
            "user": user[0],
            "jobs": jobs,
            "job_count": len(jobs),
            "bids": bids,
            "bid_count": len(bids)
        }

    return render(request, "users/profile.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')