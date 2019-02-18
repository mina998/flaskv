import random
import asyncio, aiohttp
from application.obtain import Spider
from application.db import RedisClient
from multiprocessing import Process


class Scheduler:
    # __Test_Url = ['https://www.google.com', 'https://www.github.com', 'http://www.bing.com', 'https://www.yahoo.com']
    __Test_Url = 'https://www.amazon.com'

    def get_proxy_ip(self):
        '''从网上抓取'''

        # 存方抓取时间
        methods_time = {}
        # 创建爬虫对象
        crawl = Spider()
        # 获取抓取方法
        methods = crawl.methods
        random.shuffle(methods)
        # 创建
        db = RedisClient()

        while True:
            # 如果抓取可用代理数量已达标 就等待10分钟
            if db.count() > 300:
                print('代理数量已达标 %s, 等待5分钟' % db.count())
                crawl.sleep(5*60)
                continue
            # 当前时间
            nowtime = int(crawl.time())
            # 随机取出一个抓取方法
            method = random.choice(methods)
            # 如果此方没没用过 或者 此方法上次使用时间超过30分钟 就更新使用列表
            if method not in methods_time or nowtime - methods_time[method] > 1800:

                methods_time[method] = nowtime
            # 30分钟内所有方法都使用过 就等待30分钟
            elif len(methods_time) == len(methods) and nowtime - methods_time[method] < 1800:
                print('没有可抓取的数据,等待5分钟后继续...')
                crawl.sleep(5*60)
            # 否则退出当前
            else:
                continue
            # 获取代理列表
            ips = eval('crawl.%s()' % method)
            # 如果获取失败 退出当前循环
            if not ips: continue
            try:
                loop = asyncio.get_event_loop()
                #设置并发数
                semaphore = asyncio.Semaphore(300)
                #添加任务
                tasks = [self.save_proxy_ip(semaphore,proxy) for proxy in ips]
                #执行任务
                loop.run_until_complete(asyncio.wait(tasks))
            except Exception as e:
                print('异步出错', e)


    async def save_proxy_ip(self, semaphore, ip, type = 'save'):
        '''异步保存所获取的有效代理IP'''

        # 转换ip类型
        ip = ip.decode('utf-8') if isinstance(ip,bytes) else ip
        proxy = 'http://%s' % ip

        #线程
        async with semaphore:
            #Session
            async with aiohttp.ClientSession() as session:
                try:
                    #开始验证代理
                    async with session.get(self.__Test_Url, proxy=proxy, headers=Spider().crate_headers(), timeout=3) as response:
                        #如果代理成功
                        if response.status == 200:
                            #删除Redis存在的
                            RedisClient().delete(ip)
                            #添加到Redis
                            RedisClient().add(ip)
                            print('[有效]', ip)
                        else:
                            # 删除Redis存在的
                            if type == 'check': RedisClient().delete(ip)
                            print('[无效]', ip)
                    #网络延迟3秒
                    await asyncio.sleep(3)

                except Exception as  e:

                    print('[无效]', ip)

    def check_proxy_ip(self):
        '''校验过期代理'''
        while True:
            print('验证可能过期代理...')
            # 当前抓取可用代理总数的一半
            num = RedisClient().count() // 2

            # 如果数据少于 10 等待
            if num <= 10:
                print('数据过少,等待15分钟')
                Spider().sleep(15 * 60)
            # 获取Redis中最后一半代理 等待重新验证
            ips = RedisClient().pop2(num)
            try:
                loop = asyncio.get_event_loop()
                # 设置并发数
                semaphore = asyncio.Semaphore(300)
                # 添加任务
                tasks = [self.save_proxy_ip(semaphore, ip, type='check') for ip in ips]
                # 执行任务
                loop.run_until_complete(asyncio.wait(tasks))

            except Exception as e:

                print('异步出错', e)

            print('验证完成!等待5分钟后继续, 当前代理总数 %s' % RedisClient().count())

            Spider().sleep(5 * 60)


    def run(self):
        '''运行器'''
        print('开始运行')

        get_proxy_ip  = Process(target= self.get_proxy_ip)

        check_proxy_ip= Process(target=self.check_proxy_ip)

        get_proxy_ip.start()

        check_proxy_ip.start()


if __name__ =='__main__':

    Scheduler().run()