from os import path
ROOT_PATH = path.dirname(path.realpath(__file__))

# Flask and ams Config
DEBUG = 0
# SERVER_NAME = '127.0.0.1:8080'

SQLALCHEMY_TRACK_MODIFICATIONS = 0
SQLALCHEMY_DATABASE_URI ='sqlite:///%s/data.db' % ROOT_PATH

SECRET_KEY = 'adminkfsaerwer5216821g78785623qeroiophjkjmh'

# amz Config
# 日志保存目录
LOGS_PATH  = '%s/ams/assets/logs' % ROOT_PATH
# 日志输出类型
LOG_TRACE  = 0 #1为输出显示. 0为保存到文件
# 切换城市
CHANGE_CITY = 1 #1为切换. 0为不切换
# 代理获取API
PROXY_API = 'http://127.0.0.1:1015/get?m=mina998'
# 是否使用代理
IS_PROXY = 1
