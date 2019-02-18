from flask import Flask
from ams import ams
from ams.models import db

app = Flask(__name__, static_folder='')

app.config.from_object('configure')

db.init_app(app)

app.register_blueprint(ams)


if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80)