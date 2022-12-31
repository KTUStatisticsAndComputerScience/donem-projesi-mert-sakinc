
from .connectdb import db
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_ad = db.Column(db.String)
    user_soyad = db.Column(db.String)
    user_telefon = db.Column(db.String(10), unique=True)
    user_email = db.Column(db.String)
    user_adres = db.Column(db.String)
