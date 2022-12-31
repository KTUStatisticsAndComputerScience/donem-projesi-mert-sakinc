from sqlalchemy import Column

from .connectdb import db


class cargo(db.Model):
    cargo_en = db.Column(db.Float)
    cargo_boy = db.Column(db.Float)
    cargo_yukseklik = db.Column(db.Float)
    cargo_agirlik = db.Column(db.Float)
    cargo_id = db.Column(db.BigInteger, primary_key=True)
    cargo_alici_id = db.Column(db.Integer, db.ForeignKey('kisi.kisi_id'))
    cargo_gonderici_id = db.Column(db.Integer, db.ForeignKey('kisi.kisi_id'))

    cargo_alici = db.relationship('Kisi', foreign_keys=[cargo_alici_id], backref="alici")
    cargo_gonderici = db.relationship('Kisi', foreign_keys=[cargo_gonderici_id], backref="gonderici")
