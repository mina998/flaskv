import requests
from application.db import RedisClient
from fake_useragent import UserAgent


class HttpTools(object):
    timeout = 3
    headers = None
    proxies = None

    response_code = 0
    requests_type = 'GET'

    def crate_headers(self):
        '''获取请求头信息'''
        return {'User-Agent': UserAgent().random}

    def get(self, url, headers=None):
        '''Get方法获取内容'''
        print('爬取: %s' % url)
        # 生成请求头信息
        self.headers = headers if headers else self.crate_headers()

        try:
            # 发送请求
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            # 得到响应状态码
            self.response_code = response.status_code
            # 如果页面不存在
            if response.status_code == 404:
                print('[%s]请求失败,错误代码[%s]' % (self.requests_type, response.status_code))
                return False
            # 判断如果请求成功 并返回请求内容
            if response.status_code == 200:
                return response.text
            # 使用代理发送请求
            html = self.__proxy_requests(url)
            #
            if html: return html
            #
            return False

        except Exception as e:

            # 使用代理发送请求
            return self.__proxy_requests(url)

    def post(self, url, headers=None, data=None):
        '''Post方法获取内容'''
        self.requests_type = 'POST'

        print('爬取: %s' % url)
        # 生成请求头信息
        self.headers = headers if headers else self.crate_headers()
        try:
            # 发送请求
            response = requests.post(url, headers=self.headers, data=data, timeout=self.timeout)
            # 得到响应状态码
            self.response_code = response.status_code
            # 如果页面不存在
            if response.status_code == 404:
                print('[%s]请求失败,错误代码[%s]' % (self.requests_type, response.status_code))
                return False
            # 判断如果请求成功 并返回请求内容
            if response.status_code == 200:
                return response.text
            # 使用代理发送请求
            html = self.__proxy_requests(url)
            #
            if html: return html
            #
            return False

        except Exception as e:

            # 使用代理发送请求
            return self.__proxy_requests(url)


    def __proxy_requests(self, url):

        # 执行3次
        for n in range(4):
            # 获取代理地址
            proxy = RedisClient().get()
            # 代理地址不存在 生成错误信息
            if proxy == False:
                print('[%s]请求失败,错误代码[%s][获取代理失败]' % (self.requests_type, self.response_code))
                return False
            # 生成代理格式
            proxies = {'http': proxy, 'https': proxy}
            # proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
            # 尝使用代理请求
            try:
                if self.requests_type == 'GET':
                    # GET请求
                    response = requests.get(url, proxies=proxies, headers=self.headers, timeout=self.timeout)
                else:
                    # POST请求
                    response = requests.post(url, proxies=proxies, headers=self.headers, timeout=self.timeout)
                # 得到响应状态码
                self.response_code = response.status_code
                # 判断如果请求成功 并返回请求内容
                if response.status_code == 200: return response.text
                # 创建错误信息
                print('[%s]使用代理请求失败.[%s][%s]' % (self.requests_type, response.status_code, proxy))

            except Exception as e:
                # 创建错误信息
                print('[%s]使用代理请求超时.[%s]' % (self.requests_type, proxy))

        return False
