# coding: utf-8
import requests
import time
import base64
import hmac
import hashlib
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class crashsightOpenApi(object):
    def __init__(self, x_token, app_id, app_key, request_url, body):
        self.x_token = x_token
        self.headers = {
            'Content-Type': 'application/json',
            'X-token': x_token,
            'Accept-Encoding':'*'
        }
        self.app_key = app_key
        self.request_url = request_url
        self.body = body
        self.app_id = app_id

        # 获取当前时间戳
        self.t = int(time.time())

    """
        获取签名计算值的方法
    """
    def __get_api_signature(self):
        key_bytes = bytes(self.app_id, 'utf-8')
        message = self.app_id + self.app_key + str(1626597310)
        message_bytes = bytes(message, 'utf-8')
        hash_str = hmac.new(key_bytes, message_bytes, digestmod=hashlib.sha256).hexdigest()
        # print(hash_str)

        hash_str_64 = base64.b64encode(bytes(hash_str, encoding="utf8"))
        hash_str_64 = str(hash_str_64, encoding="utf-8")
        # print(hash_str_64)

        return hash_str_64

    """
        获取相关的接口返回数据
    """
    def do_post_request(self):
        # print(self.request_url)
        self.request_url += ('?appSecret={}&appId={}&t={}'.format(self.__get_api_signature(), self.app_id, str(1626597310)))
        print(self.request_url)
        api_response = requests.post(self.request_url, data = json.dumps(self.body), headers = self.headers)
        return api_response


if __name__ == "__main__":
    # 请根据OPEN_API的文档说明，以及所在的运行环境正确填写x_token, app_id, app_key以及request_url

    x_token = 'XXX'
    app_id = 'XXX'
    app_key = 'XXX'

    #国内和海外地址不同，根据需求进行切换
    #新加坡地址
    request_url =  'https://crashsight.wetest.net/uniform/openapi/getTopIssueHourly'

    #批量openid请求
    body = {"appId":"d98b9f7eec","platformId":1,"version":"-1","countryList":[],"startHour":"2022101404","type":"crash","vm":0,"limit":5}

    crashsight_open_api_obj = crashsightOpenApi(x_token,app_id,  app_key, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)

    
