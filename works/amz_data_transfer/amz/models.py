import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, UniqueConstraint, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

base = declarative_base()


class Listing(base):
    __tablename__ = 'listing'

    id = Column(Integer, primary_key=True, autoincrement=True)
    img = Column(String(250),default='')
    asin = Column(String(15), nullable=True)
    seller = Column(String(30), default='')
    status = Column(Integer, default=0)
    adtime = Column(DateTime, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey("user.id"))

    __table_args__ = (
        # 联合唯一
        UniqueConstraint('asin', 'seller'),
    )


class Marks(base):
    __tablename__ = 'marks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bsr = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    stock = Column(String(10), nullable=True)
    uptime = Column(DateTime, default=datetime.datetime.now)
    asin_id = Column(Integer, ForeignKey("listing.id"))

    listing = relationship("Listing", backref=backref('marks'))