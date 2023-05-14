from flask import Blueprint, Response, request

bp = Blueprint("geofence", __name__)

from app.geofence import geofence
