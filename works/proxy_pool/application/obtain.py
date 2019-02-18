import re, math
from time import sleep, time
from lxml import html
from application.httptools import HttpTools
from application.functions import *

class Spider(HttpTools):

    def __init__(self):
        '''初始化'''

        self.time  = time

        self.sleep = sleep

        self.methods = list(filter(lambda m: m.startswith("cc_"), dir(self)))

        self.__Proxy_ip_list = []

    #8
    def __frees8(self,num=0):

        sre = r'<a href="(.*?)">(.*?)\s\((\d+)\)</a>'

        url = 'http://www.gatherproxy.com/proxylistbycountry'

        res = self.get(url)

        if not res: return self.__Proxy_ip_list

        urls = re.findall(sre, res)

        if not urls: return self.__Proxy_ip_list

        return urls[num]

    #8
    def cc_frees8a1(self, num=1):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #9
    def cc_frees8a2(self, num=2):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #10
    def cc_frees8a3(self, num=3):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #11
    def cc_frees8a4(self, num=4):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #12
    def cc_frees8a5(self, num=5):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #13
    def cc_frees8a6(self, num=6):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #14
    def cc_frees8a7(self, num=7):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #15
    def cc_frees8a8(self, num=8):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #16
    def cc_frees8a9(self, num=9):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #17
    def cc_frees8a10(self, num=10):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #18
    def cc_frees8a11(self, num=11):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #19
    def cc_frees8a12(self, num=12):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #20
    def cc_frees8a13(self, num=13):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #21
    def cc_frees8a14(self, num=14):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #22
    def cc_frees8a15(self, num=15):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #23
    def cc_frees8a16(self, num=16):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #24
    def cc_frees8a17(self, num=17):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #25
    def cc_frees8a18(self, num=18):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #26
    def cc_frees8a19(self, num=19):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #27
    def cc_frees8a20(self, num=20):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #28
    def cc_frees8a21(self, num=21):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #29
    def cc_frees8a22(self, num=22):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #30
    def cc_frees8a23(self, num=23):

        rows = self.__frees8(num)

        if not rows : return self.__Proxy_ip_list

        page = math.ceil(int(rows[2])/30)

        for i in range(page):

            url = 'http://www.gatherproxy.com%s%s' % (rows[0], '#%s' % (i + 1))

            url = url.replace(' ', '%20')

            data = {
                'Country': '%s' % rows[1],
                'PageIdx': '%s' % (i + 1),
                'Filter': '',
                'Uptime': '0'
            }


            res = self.post(url,data=data)

            if not res: continue

            ptn = r"write\('(\d+\.\d+\.\d+\.\d+?)'\)</script></td>[\s\S]*?<td><script>document\.write\(gp\.dep\('([\dA-F]+?)'\)\)</script></td>"
            #提取数据
            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                break

            #数据清洗
            ips = ['%s:%s' %(ip[0], int(ip[1], 16)) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    #1
    def cc_free1(self):

        url = 'https://free-proxy-list.net/'

        res = self.get(url)

        if not res: return []

        ptn = r'<td>(\d+\.\d+\.\d+\.\d+?)</td><td>(\d+?)</td>'

        ips = re.findall(ptn, res)

        if not ips:

            print('匹配失败:[%s]' % ptn)

            return []

        ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

        self.__Proxy_ip_list.extend(ips)

        return self.__Proxy_ip_list

    #2
    def cc_free2(self):
        url = 'https://www.us-proxy.org/'

        res = self.get(url)

        if not res: return []

        ptn = r'<td>(\d+\.\d+\.\d+\.\d+?)</td><td>(\d+?)</td>'

        ips = re.findall(ptn, res)

        if not ips:

            print('匹配失败:[%s]' % ptn)

            return []

        ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

        self.__Proxy_ip_list.extend(ips)

        return self.__Proxy_ip_list

    #3
    def cc_free3(self):
        url = 'https://www.socks-proxy.net/'

        res = self.get(url)

        if not res: return []

        ptn = r'<td>(\d+\.\d+\.\d+\.\d+?)</td><td>(\d+?)</td>'

        ips = re.findall(ptn, res)

        if not ips:

            print('匹配失败:[%s]' % ptn)

            return []

        ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

        self.__Proxy_ip_list.extend(ips)

        return self.__Proxy_ip_list

    #4
    def cc_free4(self):

        url = 'https://www.proxynova.com/proxy-server-list/'

        res = self.get(url)

        if not res: return self.__Proxy_ip_list

        eobj = html.etree.HTML(res)

        urls = eobj.xpath('//div[@class="dropdown"]/div[@class="col3 clearfix"]/ul/li/div/a/@href')


        for n in urls:

            url = 'https://www.proxynova.com%s'%n

            res = self.get(url)

            if not res: continue

            ptn = "write\('12345678([\d\.]+?)'\.substr\(8\)\s\+\s'([\d\.]+?)'\);</script>\s</abbr>[\s\S]*?</td>[\s\S]*?<td align=\"left\">([\s\S]+?)</td>"

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                port = ip[2].strip()

                port = re.compile(r'<[^>]+>', re.S).sub('', port)

                proxy = '%s%s:%s' % (ip[0], ip[1], port)

                self.__Proxy_ip_list.append(proxy)

        return list(set(self.__Proxy_ip_list))

    #5
    def cc_free5(self):

        url = 'https://www.xroxy.com/proxy-country/'

        res = self.get(url)

        if not res: return self.__Proxy_ip_list

        objs = html.etree.HTML(res)

        urls = objs.xpath('//div[@class="wpb_wrapper"]//ul/li/a/@href')

        for url in urls:

            res = self.get(url)

            if not res: continue

            ptn = '<td tabindex="0" class="sorting_1">(\d+\.\d+\.\d+\.\d+?)</td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

        return list(set(self.__Proxy_ip_list))

    #6
    def cc_free6(self, page = 3):

        for n in range(1,page):

            html = self.get('https://sockslist.net/proxy/server-socks-hide-ip-address/%s#proxylist' % n)

            if not html: continue

            str1 = re.findall(r'<\!\[CDATA\[([^\]]+?)\/', html)

            if not str1: break

            str1 = str1[0].replace(' ', '').strip().strip(';')
            lists= str1.split(';')

            #动态定义变量
            variable = locals()
            for items in lists:

                item = items.split('=')
                variable[item[0]] = eval(item[1] * 1)

            ptn = r't_ip">(\d+\.\d+\.\d+\.\d+?)</td>[\s\S]*?write\((.*?)\);' #匹配全部
            # ptn = r't_ip">(\d+\.\d+\.\d+\.\d+?)</td>[\s\S]*?write\((.*?)\);[\s\S]*alt="us"' #只匹配美国

            ips = re.findall(ptn, html)

            if not ips:

                print('匹配失败:[%s]' % ptn)
                continue

            for ip in ips:

                port = eval(ip[1]*1)

                proxy= '%s:%s' %(ip[0], port)

                self.__Proxy_ip_list.append(proxy)

            self.sleep(4)

        return self.__Proxy_ip_list

    #7
    def cc_free7a0(self, start=0):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a1(self, start=10):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a2(self, start=20):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a3(self, start=30):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a4(self, start=40):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a5(self, start=50):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a6(self, start=60):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a7(self, start=70):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    #7
    def cc_free7a8(self, start=80):

        import base64

        for n in range(start, start+10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:

                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:

                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' %(agent,ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a9(self, start=90):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a10(self, start=100):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a11(self, start=110):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a12(self, start=120):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a13(self, start=130):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a14(self, start=140):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a15(self, start=150):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a16(self, start=160):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 7
    def cc_free7a17(self, start=170):

        import base64

        for n in range(start, start + 10):

            url = 'https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%s' % n

            # url = 'https://www.cool-proxy.net/proxies/http_proxy_list/country_code:US/port:/anonymous:/page:%s' % n

            res = self.get(url)

            sleep(5)

            if not res: continue

            ptn = r'str_rot13\("(.*?)"\)\)\)</script></td>[\s\S]*?<td>(\d+?)</td>'

            ips = re.findall(ptn, res)

            if not ips:
                print('匹配失败:[%s]' % ptn)

                continue

            for ip in ips:
                agent = base64.b64decode(rot13(ip[0])).decode('utf-8')

                proxy = '%s:%s' % (agent, ip[1])

                self.__Proxy_ip_list.append(proxy)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 1cn
    def cc_kuaidaili(self, page=20):

        for n in range(1, page):

            html = self.get('https://www.kuaidaili.com/free/inha/%s/' % n)

            if html == False: continue

            ptn = r'data-title="IP">(.*?)</td>[\s\S]*?<td data-title="PORT">(.*?)<'

            ips = re.findall(ptn, html)

            if not ips:
                print('匹配失败:[%s]' % ptn)
                break

            ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(5)

        return self.__Proxy_ip_list

    # 2cn
    def cc_xicidaili(self, page=3):

        urls = ['https://www.xicidaili.com/nt/%s' % n for n in range(1, page)]

        for url in urls:

            html = self.get(url)

            if html == False: continue

            ptn = r'<td>(\d+\.\d+\.\d+\.\d+?)</td>[\s\S]*?<td>(\d+?)</td>[\s\S]*?<a'

            ips = re.findall(ptn, html)

            if not ips:
                print('匹配失败:[%s]' % ptn)
                break

            ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

            self.__Proxy_ip_list.extend(ips)

            self.sleep(3)

        return self.__Proxy_ip_list

    # 3cn
    def cc_31f(self):

        html = self.get('http://31f.cn/')

        if html == False: return []

        ptn = r'<td>(\d+\.\d+\.\d+\.\d+?)</td>\n<td>(\d+?)</td>'

        ips = re.findall(ptn, html)

        if not ips:
            print('匹配失败:[%s]' % ptn)
            return []

        ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

        self.__Proxy_ip_list.extend(ips)

        return self.__Proxy_ip_list

    # 4cn
    def cc_89ip(self):

        url = 'http://www.89ip.cn/tqdl.html?api=1&num=500&port=&address=&isp='

        html = self.get(url)

        if html == False: return []

        ptn = r'(\d+\.\d+\.\d+\.\d+:\d+)'

        ips = re.findall(ptn, html)

        if not ips:
            print('匹配失败:[%s]' % ptn)
            return []

        self.__Proxy_ip_list.extend(ips)

        return self.__Proxy_ip_list

    # 5cn
    def cc_free(self):

        url = 'http://lab.crossincode.com/proxy/'

        html = self.get(url)

        if html == False: return []

        pattern = r'<td>(\d+\.\d+\.\d+\.\d+?)</td>[\s\S]*?<td>(\d+?)</td>'

        ips = re.findall(pattern, html)

        ips = ['%s:%s' % (ip[0], ip[1]) for ip in ips]

        if not ips:
            print('匹配失败:[%s]' % pattern)
            return []

        self.__Proxy_ip_list.extend(ips)

        return self.__Proxy_ip_list

    #api
    def cc_apiproxy1(self):

        self.sleep(1)

        import json

        res = self.get('https://api.getproxylist.com/proxy')

        if not res: return []

        data= json.loads(res)

        ip  = '%s:%s'%(data.get('ip'),data.get('port'))

        self.__Proxy_ip_list.append(ip)

        return self.__Proxy_ip_list



if __name__ == '__main__':

    cra = Spider()
    sss = cra.cc_apiproxy1()
    print(len(sss))
    print(sss)
