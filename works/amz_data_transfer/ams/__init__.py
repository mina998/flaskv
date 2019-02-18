from flask import Blueprint

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

ams = Blueprint(
    'ams',
    __name__,
    static_folder='assets',
    template_folder='templates'
)

from . import views


# ams1 = Blueprint(
#     'ams1',
#     __name__,
#     static_folder='assets1',
#     template_folder='templates1'
# )
#
# from ams import views1