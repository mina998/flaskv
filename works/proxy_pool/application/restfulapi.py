from application.db import RedisClient
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Agent pool system'


@app.route('/get')
def get():
    if request.args.get('m') == 'mina998':

        return RedisClient().pop()
    else:
        return '111.111.111.111:111'


@app.route('/count')
def count():
    return '%s' % RedisClient().count()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=108)
