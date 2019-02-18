from redis import Redis
from random import randint

class RedisClient(Redis):

    def __init__(self):
        '''
        设置数据库存链接
        '''
        try:
            super().__init__(host='127.0.0.1')

            cf = 'stop-writes-on-bgsave-error'

            if self.config_get(cf).get(cf) == 'yes':

                self.config_set(cf, 'no')

        except Exception as e:

            print(e)

            exit()


    def get(self):
        '''随机从最后30条中取一条'''
        num = 30
        try:
            num = randint(-num, -1) if self.count()-1 > num else randint(0, self.count()-1)

            row = self.lrange('proxys', num, num)

            return row[0].decode('utf-8')

        except Exception as e:

            print('获取失败:',e)

            return False


    # 获取总长度
    def count(self):
        return self.llen('proxys')

    # 从左侧添加一个
    def add(self, proxy):

        return self.lpush('proxys', proxy)

    # 弹出右侧最后一个
    def pop(self):

        proxy = self.rpop('proxys')

        if proxy: return proxy.decode('utf-8')

        return ''

    # 从指定位置取到结尾
    def pop2(self, num):

        data = self.lrange('proxys', num, -1)

        self.ltrim('proxys', 0, num)

        return data

    # 查看所有数据
    def views(self):

        return self.lrange('proxys', 0, -1)

    # 删除指定数据
    def delete(self, value):

        return self.lrem('proxys', self.count(), value)

    def flush(self):

        self.flushall()


if __name__ == '__main__':

    db = RedisClient()

    print(db.views())

    for i in range(1,10):

        print(db.add('A%s' %i ))


