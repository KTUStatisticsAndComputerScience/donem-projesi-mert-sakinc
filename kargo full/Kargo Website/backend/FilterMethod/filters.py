import inspect
import json

from flask import request
from sqlalchemy import func

from db import db


def filtrele(dbclass):
    sorgu = db.session.query(dbclass)
    if 'sorgu' in request.args:
        talep = request.args['sorgu']
        talep_objesi = json.loads(talep)

        sinif_degiskenleri = dict(inspect.getmembers(dbclass))

        for alan in talep_objesi:
            if alan == "sirala":
                alanlar = talep_objesi[alan].split(",")
                for s_alan in alanlar:
                    if s_alan.startswith("-"):
                        sorgu = sorgu.order_by(sinif_degiskenleri[s_alan[1:]].desc())
                    elif s_alan.startswith("+"):
                        sorgu = sorgu.order_by(sinif_degiskenleri[s_alan[1:]].asc())
                    else:
                        sorgu = sorgu.order_by(sinif_degiskenleri[s_alan])
            else:
                db_f = sinif_degiskenleri[alan]
                deger = talep_objesi[alan]
                if deger.startswith(">="):
                    sorgu = sorgu.filter(db_f >= deger[2:])
                elif deger.startswith(">"):
                    sorgu = sorgu.filter(db_f > deger[1:])
                else:
                    sorgu = sorgu.filter(func.lower(db_f) == talep_objesi[alan].lower())
    return sorgu

