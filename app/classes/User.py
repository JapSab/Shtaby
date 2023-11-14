from flask import render_template, request, redirect, url_for, session
from app.classes.FormValidator import RegistrationForm, LoginForm
from app import mongo
import bcrypt


class UserHandler:
    def __init__(self):
        pass

    # def signup(self) -> str:
    #     if request.method == 'POST':
    #         username: str = request.form['username']
    #         password: str = request.form['password']

    #         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #         data = {
    #             'username': username,
    #             'password': hashed_password.decode('utf-8')
    #         }

    #         collection = mongo.db.users
    #         collection.insert_one(data)
    #         session['username'] = username

    #         return redirect(url_for('homePage'))
    #     return render_template('form.html')
    def signup(self) -> str:
        form = RegistrationForm()

        if request.method == 'POST' and form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            data = {
                'username': username,
                'password': hashed_password.decode('utf-8')
            }

            collection = mongo.db.users
            collection.insert_one(data)
            session['username'] = username

            return redirect(url_for('homePage'))
        return render_template('form.html', form=form)

    def login(self):
        form = LoginForm()

        if request.method == 'POST' and form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            collection = mongo.db.users
            is_user = collection.find_one({'username': username})

            if is_user and bcrypt.checkpw(password.encode('utf-8'), is_user['password'].encode('utf-8')):
                session['authenticated'] = True
                return redirect(url_for('homePage'))
            else:
                return 'Invalid user credentials.'  # Use flash to display an error message

        return render_template('login.html', form=form)