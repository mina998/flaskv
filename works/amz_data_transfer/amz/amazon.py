import requests, re, json, time
from fake_useragent import UserAgent
from lxml import html
from random import choice
from configure import LOGS_PATH, PROXY_API, CHANGE_CITY, LOG_TRACE, IS_PROXY


class GetProductInfo:

    __instance = None
    __proxies = None
    __price = False
    __stock = False

    __bsr = False
    __sid = False
    __oid = False
    __uid = False
    __img = None

    def __init__(self, asin, seller=None):
        '''初始化类构建所需要参数'''
        # 是否使用代理
        self.__is_proxy = IS_PROXY
        # 日志输出方式
        self.__cmd = LOG_TRACE
        # 是否更改城市
        self.__change = CHANGE_CITY
        # 查询ASIN
        self.__asin = asin
        # 卖家ID
        self.__seller = None if not seller else seller
        # 模拟浏览器
        self.__headers = {'user-agent': UserAgent().chrome}

        # 设置重连次数
        requests.adapters.DEFAULT_RETRIES = 5
        self.__session = requests.session()
        self.__session.keep_alive = False

    def get(self):
        '''获取Asin数据'''

        # 1.更改所在城市
        if not self.__change_city(): return False
        # 2.发送请求
        htmlStr = self.__send()
        if not htmlStr: return False
        # 3.获取产品页数据
        if not self.__page1(htmlStr): return False

        if self.__cmd : print('产品页库存：', self.__stock)

        if self.__stock:
            return {'img': self.__img, 'bsr': self.__bsr, 'stock': self.__stock, 'price': self.__price}
        # 4.POST查询库存
        time.sleep(3)
        if not self.__page2():return False

        if self.__cmd : print('购物车查询：', self.__stock)

        return {'img': self.__img, 'bsr': self.__bsr, 'stock': self.__stock, 'price': self.__price}

    def __change_city(self):

        if not self.__change: return False

        url = 'https://www.amazon.com/gp/delivery/ajax/address-change.html'

        posts = [10001,10002,10014,20038,94111,94144]

        data = {
            'locationType': 'LOCATION_INPUT',
            'zipCode': choice(posts),
            'storeContext': 'home-garden',
            'deviceType': 'web',
            'pageType': 'Detail',
            'actionSource': 'glow'
        }
        try:

            for i in range(2):

                response = self.__session.post(url, headers=self.__headers, params=data)

                if json.loads(response.text).get('address').get('countryCode') == 'US': return True

                self.__trace_log(False, '切换城市失败!')
            return False

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

            for i in range(4):
                time.sleep(1)
                # 发送请求
                response = self.__session.get(url, headers=self.__headers, proxies=self.__proxies, timeout=8)
                cookie = requests.utils.dict_from_cookiejar(response.cookies)

                self.__uid = cookie.get('ubid-main') if cookie.get('ubid-main') else '000-0000000-0000000'

                # HTTP请求状态错误
                if response.status_code != 200:
                    if self.__trace_log(False, '[%s]HTTP请求状态错误'% response.status_code): continue

                # 获取代码为空
                if not response.text:
                    if self.__trace_log(False, '获取代码为空!'): continue

                # 页面出现验证码
                if 'Type the characters you see in this image:' in response.text:
                    time.sleep(1)
                    if self.__get_proxy() and i < 3:

                        self.__trace_log(False, '出现验证码,尝试使用代理 [%s]'% self.__proxies.get('http'))

                        continue
                        
            time.sleep(3)

            return response.text

        except Exception as e:

            proxy = '代理地址:[%s]' % self.__proxies.get('http') if self.__proxies else ''

            if self.__trace_log(False, '产品页HTTP请求错误! %s' % proxy): return False

    def __page1(self, htmlStr):
        '''获取产品页面数据'''

        # 产品图片
        img = re.findall(r'colorImages\'.*?(https.*?)"', htmlStr, re.I)
        self.__img = None if not img else img[0]

        # 获取页面SessionID
        sid = re.findall(r'id="session-id" name="session-id" value="(.+)?">', htmlStr, re.I)
        self.__sid = sid[0] if len(sid) > 0 else self.__sid

        if self.__trace_log(self.__sid, '获取参数SessionID失败'): return False

        # 获取页面OfferListingID
        oid = re.findall(r'name=\"offerListingID\" value=\"(.+?)\"', htmlStr, re.I)
        self.__oid = oid[0] if len(oid) > 0 else self.__oid
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
        # self.__headers["cookie"] = "session-id=%s; ubid-main=000-0000000-0000000;" % self.__sid
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

            if self.__trace_log(self.__stock, '获取库存失败.%s'% stock): return False

            return True

        except Exception as e:

            if self.__trace_log(False, '查询库存失败:%s'%e): return False

    def __trace_log(self, ss, log):

        #print('Test:',ss)

        if not ss:

            if self.__cmd == False:
                file = LOGS_PATH+'/trace.txt'
                with open(file, 'a+', encoding='utf-8') as fb:
                    fb.write('[%s][%s] %s\n' % (self.__asin, self.__notime(), log))
            else:
                print('[%s][%s] %s' % (self.__asin, self.__notime(), log))

            return True

        return False

    def __get_proxy(self):

        try:

            res = requests.get(PROXY_API)

            if res.status_code == 200 and res.text:

                self.__proxies = {'http': res.text, 'https': res.text}

                return self.__proxies

            self.__trace_log(False, '获取不到代理')

            return False

        except Exception as e:

            self.__trace_log(False,'与API链接失败')

        return False

    # 当前时间
    def __notime(self):

        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

if __name__ == '__main__':


    data = GetProductInfo('B07KLVKTPP',seller='').get()

    print(data)


