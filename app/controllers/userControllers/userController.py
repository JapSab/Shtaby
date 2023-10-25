from flask import render_template, request, Flask, redirect, url_for, session
from app import app
from app.classes.User import UserHandler

# instance of the UserHandler class
user_handler = UserHandler()

# routes
@app.route('/signup', methods=['GET', 'POST'])
def contact_form() -> str:
    return user_handler.signup()

@app.route('/login', methods=['GET', 'POST'])
def login_form() -> str:
    return user_handler.login()
