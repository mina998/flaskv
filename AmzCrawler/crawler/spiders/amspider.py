import random, json, re, requests
from scrapy import Spider, Request, FormRequest
from crawler.db import sqlite


class TSpider(Spider):
    name = 'amazon'
    # 切换城市URL链接
    __change_cidy_url = 'https://www.amazon.com/gp/delivery/ajax/address-change.html'
    # 邮编
    __zipcode = [10001, 10002, 10014, 20038, 94111, 94144]


    def start_requests(self):

        while True:

            urls = self.__get_urls()

            if not urls: break

            for i, row in enumerate(urls):

                query = '/?m=%s' % row[2] if row[2] else ''

                url = 'https://www.amazon.com/dp/{asin}{query}'.format(asin = row[1], query = query)

                cookies = self.__get_cidy_cookies()

                if cookies: yield Request(url, cookies=cookies, meta={'id':row[0],'asin':row[1],'cookiejar': i})

        sqlite.execute('update listing set status = 0 where status = 1')

        sqlite.commit()

        sqlite.close()


    def parse(self, response):

        html = response.body.decode('utf-8')
        item = {}

        # 获取页面SessionID
        sid = response.xpath('//input[@id="session-id"]/@value').extract_first()
        # 获取页面OfferListingID
        oid = response.xpath('//input[@id="offerListingID"]/@value').extract_first()

        item['id'] = response.meta['id']
        # 获取查询ASIN
        item['asin'] =  response.meta['asin']
        # 产品图片
        item['img'] = re.findall(r'colorImages\'.*?(https.*?)"', html, re.I)
        # # 获取BSR排名
        item['bsr'] = re.findall(r"#([\d,]+)\sin.*See top 100.*</a>\)", html, re.I)
        # # 获取产品价格
        item['price'] = re.findall(r'id=\"priceblock_ourprice.*?>\$([\d.]+)<', html, re.I)

        # 获取产品库存
        item['stock'] = re.findall(r'Only (\d+?) left in stock - order soon.', html, re.I)


        if not item['price']:
            with open('./%s.html' % item['asin'], 'w+', encoding='utf-8') as f:
                f.write(html)

        # 查询卖是否限制购卖数量
        if item['stock']:

            item['stock'] = item['stock'][0]

            yield item

        else:
            stock = len(response.xpath('//select[@id="quantity"]/option/@value').extract())

            if stock < 30 and stock > 0:

                item['stock'] = stock

                yield item
            else:
                # 请求地址
                url = "https://www.amazon.com/gp/add-to-cart/json/ref=dp_start-bbf_1_glance"
                # 构造发送数据
                data = {
                    'clientName': 'SmartShelf',
                    'ASIN': '%s' % item['asin'],
                    'verificationSessionID': '%s' % sid,
                    'offerListingID': '%s' % oid,
                    'quantity': '99999'
                }

                cookies = {
                    "session-id": "%s" % sid,
                    "ubid-main": "000-0000000-0000000"
                }

                meta = {'item': item, 'cookiejar': response.meta['cookiejar']}

                yield FormRequest(url, cookies=cookies, meta=meta, formdata=data, callback=self.__stock)


    def __stock(self, response):
        '''
        查询库存
        '''
        item = response.meta['item']

        jsons = response.body.strip().decode('utf-8')

        stock = json.loads(jsons)

        item['stock'] = stock.get('cartQuantity')

        yield item


    def __get_cidy_cookies(self):

        data = {
            'locationType': 'LOCATION_INPUT',
            'zipCode': random.choice(self.__zipcode),
            'storeContext': 'home-garden',
            'deviceType': 'web',
            'pageType': 'Detail',
            'actionSource': 'glow'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

        try:
            response = requests.post(self.__change_cidy_url, headers=headers, params=data)

            if json.loads(response.text).get('address').get('countryCode') == 'US':
                cookies = requests.utils.dict_from_cookiejar(response.cookies)

                return cookies

            return False

        except Exception as e:

            return False

    def __get_urls(self):

        sql = 'select id,asin,seller from listing where status =0 limit 10'

        rows= sqlite.execute(sql).fetchall()

        return rows