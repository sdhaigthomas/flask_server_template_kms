#imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#create db obj
db = SQLAlchemy()

#create loginman
login_manager = LoginManager()