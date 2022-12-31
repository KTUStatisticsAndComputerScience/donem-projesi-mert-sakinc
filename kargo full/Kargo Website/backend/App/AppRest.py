from flask import Blueprint, jsonify, request

from FilterMethod import filters
from db import db


def AppRest(cargo, dbclass, semaclass):
    bp = Blueprint(cargo, __name__)

    @bp.route("/", methods=["GET"])
    def tumu():
        kayitlar = filters(dbclass)
        sema = semaclass()
        return sema.dump(kayitlar, many=True)
    @bp.route("/sayfa/<int:kayit_sayisi>/<int:sayfa_no>")
    def sayfa(kayit_sayisi, sayfa_no):
        sayfa_no -= 1
        atlanacak_kayit_sayisi = kayit_sayisi * sayfa_no
        getirilecek_kayit_sayisi = kayit_sayisi
        kayitlar = filters(dbclass).offset(atlanacak_kayit_sayisi).limit(getirilecek_kayit_sayisi).all()
        sema = semaclass()
        return sema.dump(kayitlar, many=True)
    @bp.route("/<int:id>", methods=["GET"])
    def detay(id):
        cargo = db.get_or_404(dbclass, id)
        sema = semaclass()
        return sema.dump(cargo)

    @bp.route("/sayfa/<int:kayit_sayisi>")
    def sayfa_sayisi(kayit_sayisi):
        kargo_sayisi = filters(dbclass).count()
        sayfa_sayisi = kargo_sayisi // kayit_sayisi
        if kargo_sayisi % kayit_sayisi > 0:
            sayfa_sayisi += 1
        return jsonify({"kayit_sayisi": kargo_sayisi, "sayfa_sayisi": sayfa_sayisi})
    @bp.route("/", methods=["POST"])
    def ekle():
        yeni_kayit = request.json
        yeni = dbclass(**yeni_kayit)
        db.session.add(yeni)
        db.session.commit()
        sema = semaclass()
        return sema.dump(yeni)
    @bp.route("/<int:id>", methods=["PUT", "PATCH"])
    def guncelle(id):
        kayit = db.get_or_404(dbclass, id)
        kayit_bilgileri = request.json
        sema = semaclass()
        yeni_kargo = sema.load(kayit_bilgileri, instance=kayit, session=db.session)
        db.session.commit()
        return sema.dump(yeni_kargo)
    @bp.route("/<int:id>", methods=["DELETE"])
    def sil(id):
        kayit = db.get_or_404(dbclass, id)
        db.session.delete(kayit)
        db.session.commit()
        return jsonify({"sonuc": "Silindi"})
    return bp
