import os
from flask import render_template, request, Flask, redirect
from werkzeug.utils import secure_filename
from app import app
from app.classes.Drive import Drive
 
DRIVE_FOLDER = 'Drive'
app.config['UPLOAD_FOLDER'] = DRIVE_FOLDER
driveInstance = Drive()        

@app.route('/drive')
def upload():
    return driveInstance.drivePage()

@app.route('/uploader', methods = ['GET', 'POST'])
def file_upload():
    return driveInstance.uploader()
    