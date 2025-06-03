#imports
from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from utils.username_val import username_val
from utils.email_val import email_val
from utils.encryption import make_hash, check
from extensions import login_manager, db
from models.user import User

#makes blueprint object 
def setup(name:str)->object:
    return Blueprint(name, __name__)

@login_manager.user_loader
def load_user(user_id:int)->object:
    return User.query.get(user_id)