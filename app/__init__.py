from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config.from_object('config')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ShtabyBase'
mongo = PyMongo(app)
app.template_folder = 'views/templates'
app.static_folder = 'static'

from app.controllers.userControllers import userController

