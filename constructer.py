#imports
from flask import Flask, make_response, render_template
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from blueprints.non_auth import non_auth
from blueprints.auth import auth
from extensions import db, login_manager
from keys import get_key

#app factory
def create_app()->object:
    #app abject
    app = Flask(__name__)

    #blueprints registered
    app.register_blueprint(non_auth)
    app.register_blueprint(auth)

    #database shi
    app.config['SECRET_KEY'] = get_key()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/database.db"

    #import all models here
    from models.user import User

    #init the db
    db.init_app(app)

    #make the db file, if not already there
    with app.app_context():
        db.create_all()

    #css page
    @app.route('/style.css')
    def css():
        resp = make_response(render_template("style.css"))
        resp.headers['Content-type'] = 'text/css'
        return resp

    #define login obj
    login_manager.init_app(app)

    if __name__ == '__main__':
        #start app
        app.run()

create_app()