#FLASK SETTINGS
from flask import Flask
app = Flask(__name__)

#API SETTINGS
from flask_restful import Resource, Api
api = Api(app)

#DATABASE SETTINGS
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

#BCRYPT SETTINGS
from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from app import views
