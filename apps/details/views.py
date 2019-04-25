from django.shortcuts import render, redirect
from mysqlconnection import connectToMySQL

# Create your views here.

def jobdetails(request, job_id):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        mysql = connectToMySQL('bid_dash')
        data = {'user_id': request.session['user_id']}
        user = mysql.query_db('SELECT * FROM users WHERE id = %(user_id)s;', data)

        mysql = connectToMySQL('bid_dash')
        data = {'job_id': job_id}
        job_details = mysql.query_db('SELECT j.id as job_id, j.users_id as poster_id, j.title, j.description, j.max_price, j.start_datetime, j.end_datetime, a.city, u.first_name, u.last_name FROM jobs j JOIN addresses a ON j.addresses_id = a.id JOIN users u ON j.users_id = u.id WHERE j.id = %(job_id)s;', data)

        mysql = connectToMySQL('bid_dash')
        data = {'job_id': job_id}
        bids_placed = mysql.query_db('SELECT b.id, b.amount, b.chosen_bid, b.users_id AS bidder_id, u.first_name, u.last_name, u.rating, b.created_at FROM bids b JOIN users u ON b.users_id = u.id WHERE jobs_id = %(job_id)s ORDER BY amount;', data)

        context = {
            "user": user[0],
            "job": job_details[0],
            "bids_count": len(bids_placed),
            "bids": bids_placed
        }

    return render(request, "details/details.html", context)

def postbid(request):
    mysql = connectToMySQL('bid_dash')
    data = {'job_id': request.POST['job_id'], 'poster_id': request.POST['poster_id'], 'bid_amt': request.POST['bid_amt'], 'bidder_id': request.session['user_id']}
    mysql.query_db('INSERT INTO bids (jobs_id, jobs_users_id, amount, users_id) VALUES(%(job_id)s, %(poster_id)s, %(bid_amt)s, %(bidder_id)s);', data)

    return redirect('/details/'+request.POST['job_id'])

def choosebid(request, job_id, bid_id):
    mysql = connectToMySQL('bid_dash')
    data = {'job_id': job_id, 'bid_id': bid_id}
    mysql.query_db('UPDATE bids SET chosen_bid = 0 WHERE jobs_id = %(job_id)s;', data)

    mysql = connectToMySQL('bid_dash')
    mysql.query_db('UPDATE bids SET chosen_bid = 1 WHERE id = %(bid_id)s AND jobs_id = %(job_id)s;', data)

    return redirect('/details/'+job_id)

def logout(request):
    request.session.clear()
    return redirect('/')