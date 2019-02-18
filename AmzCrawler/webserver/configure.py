from os import path,sep
ROOT_PATH = sep.join(path.dirname(path.realpath(__file__)).split(sep)[:-1])+sep

# Flask and ams Config
DEBUG = 0
# SERVER_NAME = '127.0.0.1:8080'

SQLALCHEMY_TRACK_MODIFICATIONS = 0
SQLALCHEMY_DATABASE_URI ='sqlite:///%s/data.db' % ROOT_PATH

SECRET_KEY = 'adminkfsaerwer5216821g78785623qeroiophjkjmh'

# amz Config
# 日志保存目录
LOGS_PATH  = '%s/ams/assets/logs' % ROOT_PATH
