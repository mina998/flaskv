import requests, re, json, time
from fake_useragent import UserAgent
from lxml import html
from random import choice
from configure import LOGS_PATH


class GetProductInfo:

    __instance = None
    __price = False
    __stock = False

    __bsr = False
    __sid = False
    __oid = False
    __uid = False
    __img = None

    def __init__(self, asin, seller=None, proxy=None, cmd=False, change = 1):
        '''初始化类构建所需要参数'''
        self.__cmd = cmd
        # 是否更改城市
        self.__change = change
        # 当前时间
        self.__notime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 查询ASIN
        self.__asin = asin
        # 卖家ID
        self.__seller = None if not seller else seller
        # 模拟浏览器
        self.__headers = {'user-agent': UserAgent().chrome}
        # 创建代理
        self.__proxies = {'http': proxy, 'https': proxy} if proxy else proxy

        self.__session = requests.session()

    def get(self):
        '''获取Asin数据'''

        # 1.更改所在城市
        if self.__change:
            self.__change_city()
            time.sleep(5)
        # 2.发送请求
        htmlStr = self.__send()
        time.sleep(5)
        if not htmlStr: return False

        # 3.获取产品页数据
        if not self.__page1(htmlStr): return False

        if self.__stock:
            return {'img': self.__img, 'bsr': self.__bsr, 'stock': self.__stock, 'price': self.__price}

        if not self.__page2(): return False

        return {'img': self.__img, 'bsr': self.__bsr, 'stock': self.__stock, 'price': self.__price}

    def __change_city(self):

        url = 'https://www.amazon.com/gp/delivery/ajax/address-change.html'

        posts = [10001,10002,10014,20038,94101,94144]

        data = {
            'locationType': 'LOCATION_INPUT',
            'zipCode': choice(posts),
            'storeContext': 'home-garden',
            'deviceType': 'web',
            'pageType': 'Detail',
            'actionSource': 'glow'
        }
        try:
            response = self.__session.post(url, headers=self.__headers, params=data)

            if json.loads(response.text).get('address').get('countryCode') != 'US':

                if self.__trace_log(False, '切换城市失败!'): return False

        except Exception as e:

            if self.__trace_log(False, '切换城市连接超时!'): return False

        cookie = requests.utils.dict_from_cookiejar(response.cookies)

        self.__sid = cookie.get('session-id')

    def __send(self, ):

        '''发送请求'''

        # 生成查询参数
        query = '/?m=%s' % self.__seller if self.__seller else ''
        # 生成产品链接地址
        url = 'https://www.amazon.com/dp/%s%s' % (self.__asin, query)

        if self.__cmd: print(url)


        try:
            # 发送请求
            response = self.__session.get(url, headers=self.__headers, proxies=self.__proxies, timeout=15)
            response.encoding = 'utf-8'

            cookie = requests.utils.dict_from_cookiejar(response.cookies)
            self.__uid = cookie.get('ubid-main') if cookie.get('ubid-main') else '000-0000000-0000000'

            # HTTP请求状态错误
            if response.status_code != 200:

                if self.__trace_log(False, 'HTTP请求状态错误'): return False

            # 获取代码为空
            if not response.text:

                if self.__trace_log(False, '获取代码为空!'): return False

            # 页面出现验证码
            if 'Type the characters you see in this image:' in response.text:

                time.sleep(5*60)

                if self.__trace_log(False, '出现验证码,已等待5分钟!'): return False

            return response.text

        except Exception as e:

            if self.__trace_log(False, '产品页HTTP连接错误!'): return False

    def __page1(self, htmlStr):
        '''获取产品页面数据'''

        # 产品图片
        img = re.findall(r'initial\': \[\{"hiRes":"(.*?)",', htmlStr, re.I)
        self.__img = None if not img else img[0]

        # 获取页面SessionID
        if not self.__sid:
            sid = re.findall(r'id="session-id" name="session-id" value="(.+)?">', htmlStr, re.I)
            if len(sid) > 0: self.__sid = sid[0]

        if self.__trace_log(self.__sid, '获取参数SessionID失败'): return False

        # 获取页面OfferListingID
        oid = re.findall(r'name=\"offerListingID\" value=\"(.+?)\"', htmlStr, re.I)
        if len(oid) > 0: self.__oid = oid[0]
        if self.__trace_log(self.__oid, '获取参数OfferListingID失败'): return False

        # 获取BSR排名
        bsr = re.findall(r"#([\d,]+)\sin.*See top 100.*</a>\)", htmlStr, re.I)
        self.__bsr = bsr[0].replace(',', '') if len(bsr) > 0 else False
        if self.__trace_log(self.__bsr, '获取排名失败'): return False

        # 获取产品价格
        price = re.findall(r'id=\"priceblock_ourprice.*?>\$([\d.]+)<', htmlStr, re.I)
        self.__price = price[0] if len(price) > 0 else False
        if self.__trace_log(self.__price, '获取价格失败'): return False

        # 获取产品库存
        stock = re.findall(r'Only (\d+?) left in stock - order soon.', htmlStr, re.I)
        self.__stock = False if not stock else stock[0]
        # 查询卖是否限制购卖数量
        if not stock:
            eobj = html.etree.HTML(htmlStr)
            stock = len(eobj.xpath('//select[@id="quantity"]/option/@value'))

            self.__stock = stock if stock < 30 else False

        return True

    def __page2(self):
        '''查询库存数量'''

        # 请求地址
        url = "https://www.amazon.com/gp/add-to-cart/json/ref=dp_start-bbf_1_glance"
        # 构造请求头
        self.__headers["cookie"] = "session-id=%s; ubid-main=%s;" % (self.__sid, self.__uid)
        # 构造发送数据
        data = {
            'clientName': 'SmartShelf',
            'ASIN': self.__asin,
            'verificationSessionID': self.__sid,
            'offerListingID': self.__oid,
            'quantity': '99999'
        }

        try:
            response = self.__session.post(url, headers=self.__headers, params=data)

            if response.status_code != 200: return False

            stock = json.loads(response.text)

            if stock.get('isOK'):
                self.__stock = stock.get('cartQuantity') if stock.get('cartQuantity') else '-1'

            if self.__trace_log(self.__stock, '获取库存失败'): return False

            return True

        except Exception as e:

            if self.__trace_log(False, '查询库存HTTP链接失败!'): return False

    def __trace_log(self, ss, log):

        # print('Test:',ss)

        if not ss:

            if self.__cmd == False:
                file = LOGS_PATH+'\\trace.txt'
                with open(file, 'a+', encoding='utf-8') as fb:
                    fb.write('[%s][%s] %s\n' % (self.__asin, self.__notime, log))
            else:
                print('[%s][%s] %s' % (self.__asin, self.__notime, log))

            return True

        return False

    def __new__(cls, *args, **kwargs):

        if cls.__instance == None:
            cls.__instance = object.__new__(cls)

        return cls.__instance


if __name__ == '__main__':

    proxy = None

    for n in range(2):

        # proxy = requests.get('http://198.35.45.110/get?m=mina998').text
        #
        # print(proxy)

        data = GetProductInfo('B07KLVKTPP',cmd=1).get()

        print(data)

        import time

        time.sleep(5)
