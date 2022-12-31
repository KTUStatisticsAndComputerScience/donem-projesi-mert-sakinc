from db import cargo, User
from .ma import ma

class UserSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class cargoSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cargo
        include_fk = True
        load_instance = True
