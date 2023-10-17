from flask import render_template, request, Flask, redirect, session
from app import app

@app.route('/home', methods=['GET'])
def homePage():
    if session.get('authenticated'):
        return 'Hello '
    else:
        return redirect('/login')