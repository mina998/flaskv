from os import path
ROOT_PATH = path.dirname(path.realpath(__file__))

# Flask and ams Config
DEBUG = 1
# SERVER_NAME = '127.0.0.1:8080'

SQLALCHEMY_TRACK_MODIFICATIONS = 0
SQLALCHEMY_DATABASE_URI ='sqlite:///%s/data.db' % ROOT_PATH

SECRET_KEY = 'adminkfsaerwer5216821g78785623qeroiophjkjmh'

# amz Config
# 日志保存目录
LOGS_PATH  = '%s/ams/assets/logs' % ROOT_PATH
# 日志输出类型
LOG_TRACE  = 1
# 切换城市
CHANGE_CITY = 1