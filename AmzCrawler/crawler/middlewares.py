from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):


    def process_request(self, request, spider):

        ua = UserAgent().chrome

        request.headers['User-Agent'] = ua



    def process_response(self, request, response, spider):

        # 页面出现验证码
        if 'Type the characters you see in this image:' in response.body.decode('utf-8'):

            print('出现验证码,尝试使用代理')

            return request

        return response
