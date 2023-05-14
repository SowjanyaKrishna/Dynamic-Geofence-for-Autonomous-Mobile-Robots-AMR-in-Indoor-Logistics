"""
In this file all the Data Models that are beeing saved in the DB are being created.

See sqlalchemy and flask sqlalchemy for documentation

"""
from app import db
from app import ma
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import url_for, current_app
from hashlib import md5
from secrets import token_urlsafe
from datetime import datetime, timedelta, date
from logging import info, warning
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import scoped_session, sessionmaker


class User(db.Model):
    # example of a User class you can delete or rename
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = generate_password_hash(password, method="sha256")

    @classmethod
    def authenticate(cls, **kwargs):
        name = kwargs.get("name")
        password = kwargs.get("password")

        if not name or not password:
            return None

        user = cls.query.filter_by(name=name).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class SpeedRange(db.Model):
    __tablename__ = "speedrange"

    id = db.Column(db.Integer, primary_key=True)
    upperlimit = db.Column(db.Float, nullable=False)
    lowerlimit = db.Column(db.Float, nullable=False)
    offset = db.Column(db.Float, nullable=False)


# Session = scoped_session( sessionmaker() )
class SpeedRangeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SpeedRange
        load_instance = True


class MqttTopics(db.Model):
    __tablename__ = "MQTT"

    id = db.Column(db.Integer, primary_key=True)
    AGVName = db.Column(db.String(120), nullable=False)
    AGVTopic = db.Column(db.String(120), nullable=False)
    GeofenceId = db.Column(db.String(120), nullable=False)
    NaiseTag = db.Column(db.String(120), nullable=False)


class MqttTopicsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MqttTopics
        load_instance = True
