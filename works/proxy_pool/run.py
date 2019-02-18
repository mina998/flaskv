from application.dispatch import Scheduler as g
from application.restfulapi import app

'''
运行本程序需要以下模块支持:

flask
requests
redis
fake_useragent
aiohttp

'''


def main():
    g().run()
    app.run(host='0.0.0.0', port=1015)


if __name__ == '__main__':
    main()
