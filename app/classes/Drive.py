import os
from flask import render_template, request, Flask, redirect
from werkzeug.utils import secure_filename
from app import app

class Drive:
    def __init__(self):
        pass
    
    def drivePage(self):
        return render_template('drive.html')
        
    def uploader(self) -> str:
        if request.method == 'POST':
            f = request.files['file']
            if f:
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok = True) 
                filename = secure_filename(f.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                f.save(filepath)
            return 'file uploaded successfully'