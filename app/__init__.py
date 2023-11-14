from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os 
load_dotenv()

app = Flask(__name__)

app.config.from_object('config')
app.config['MONGO_URI'] = os.getenv('DATABASE_URI')
mongo = PyMongo(app)
app.template_folder = 'views/templates'
app.static_folder = 'static'
app.secret_key = os.getenv('SECRET_KEY')

from app.controllers.userControllers import userController
from app.controllers.homeController import homeController
from app.controllers.driveController import driveController
