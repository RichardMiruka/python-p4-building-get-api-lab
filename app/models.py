from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    baked_goods = db.relationship('BakedGood', backref='bakery', lazy=True)

    def to_dict(self, include_baked_goods=False):
        bakery_dict = {
            'id': self.id,
            'name': self.name,
        }
        if include_baked_goods:
            bakery_dict['baked_goods'] = [baked_good.to_dict() for baked_good in self.baked_goods]
        return bakery_dict

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
        }

    