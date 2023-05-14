from flask import (
    Flask,
)  # flask is the package and Flask is the application class from package
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from app import cli
import sqlite3


import locale

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    locale.setlocale(locale.LC_TIME, "")  # To set the local time locale is used here

    app = Flask(
        __name__
    )  # Creation of an instance for the class, to locate the application for flask. _name_ is name of package here geofence.py
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    migrate.init_app(app, ma)

    with app.app_context():
        from app.geofence import geofence

        db.create_all()

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    from app.geofence import bp as geofence_bp

    app.register_blueprint(geofence_bp, url_prefix="/api")

    from app.utilities import bp as utilities_bp

    app.register_blueprint(utilities_bp, url_prefix="/api")

    cli.register(app)

    return app


from app import models
