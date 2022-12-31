from flask import Blueprint

from db import cargo, User

from Marsh-Sema import cargoSema, UserSema

from App import AppRest

v1 = Blueprint('v1', __name__)
v1.register_blueprint(AppRest("Kargolar", cargo, cargoSema), url_prefix="/Kargolar")
v1.register_blueprint(AppRest("Kisiler", User, UserSema), url_prefix="/Kisiler")

api = Blueprint('api', __name__)
api.register_blueprint(v1, url_prefix="/v1")