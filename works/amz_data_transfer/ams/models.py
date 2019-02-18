import datetime

from ams import db

class Listing(db.Model):
    __tablename__ = 'listing'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(250), default='')
    asin = db.Column(db.String(15), nullable=True)
    seller = db.Column(db.String(30), default='')
    status = db.Column(db.Integer, default=0)
    adtime = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    __table_args__ = (
        # 联合唯一
        db.UniqueConstraint('asin', 'seller'),
    )


class Marks(db.Model):
    __tablename__ = 'marks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bsr = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.String(10), nullable=False)
    uptime = db.Column(db.DateTime, default=datetime.datetime.now)

    asin_id = db.Column(db.Integer, db.ForeignKey("listing.id"))

    listing = db.relationship("Listing", backref=db.backref('marks'))


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pwd = db.Column(db.String(40), nullable=True)
    name = db.Column(db.String(10), nullable=True, unique=True)
