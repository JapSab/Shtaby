from flask import render_template, request, Flask, redirect, url_for, session
from app import mongo
import bcrypt


class UserHandler:
    def __init__(self):
        pass

    def signup(self) -> str:
        if request.method == 'POST':
            username: str = request.form['username']
            password: str = request.form['password']

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            data = {
                'username': username,
                'password': hashed_password.decode('utf-8')
            }

            collection = mongo.db.users
            collection.insert_one(data)
            session['username'] = username

            return redirect(url_for('homePage'))
        return render_template('form.html')

    def login(self) ->str:
        if request.method == 'POST':
            username: str = request.form['username']
            password: str = request.form['password']

            collection = mongo.db.users
            is_user = collection.find_one({'username': username})

            if is_user and bcrypt.checkpw(password.encode('utf-8'), is_user['password'].encode('utf-8')):
                session['authenticated'] = True
                return redirect(url_for('homePage'))
            else:
                return 'Invalid user credentials.'
        return render_template('login.html')