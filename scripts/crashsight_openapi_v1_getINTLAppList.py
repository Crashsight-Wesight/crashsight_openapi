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
    def __init__(self, x_token, app_id, app_key, request_url):
        self.x_token = x_token
        self.headers = {
            'Content-Type': 'json',
            'X-token': x_token,
            'Accept-Encoding':'*'
        }
        self.app_id = app_id
        self.app_key = app_key
        self.request_url = request_url

        # 获取当前时间戳
        self.t = int(time.time())


    """
        获取签名计算值的方法
    """
    def __get_api_signature(self):
        key_bytes = bytes(self.app_id, 'utf-8')
        message = self.app_id + self.app_key + str(self.t)
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
    def do_get_request(self):
        self.request_url += ('&appSecret={}&appId={}&t={}'.format(self.__get_api_signature(), self.app_id, str(self.t)))
        print(self.request_url)

        api_response = requests.get(self.request_url, headers=self.headers, verify=False)
        return api_response


if __name__ == "__main__":
    # 请根据OPEN_API的文档说明，以及所在的运行环境正确填写x_token, app_id, app_key以及request_url

    x_token = 'XXX'
    app_id = 'XXX'
    app_key = 'XXX'

    #IEGG地址
    request_url =  'https://crashsight-sg.iegcom.com/uniform/openapi/getINTLAppList/56310?noNeedMemberCount=false'

    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(x_token, app_id, app_key, request_url)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)
