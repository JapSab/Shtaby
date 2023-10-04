from flask import render_template, request, Flask, redirect
from app import app
from app import mongo

@app.route('/signup', methods=['GET','POST'])
def contact_form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        data = {
            'username': username,
            'password': password
        }

        collection = mongo.db.users
        collection.insert_one(data)
        return f"Account successfully registered"

    return render_template('form.html')

