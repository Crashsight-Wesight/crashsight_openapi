# coding: utf-8
import requests
import time
import base64
import hmac
import hashlib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class crashsightOpenApi(object):
    def __init__(self,localUserId, userOpenapiKey, request_url):
        self.localUserId = localUserId
        self.headers = {
            'Content-Type': 'application/json',
            'Accept-Encoding':'*'
        }
        self.userOpenapiKey = userOpenapiKey
        self.request_url = request_url
        self.localUserId = localUserId

        # 获取当前时间戳
        self.t = int(time.time())

    """
        获取签名计算值的方法
    """
    def __get_api_signature(self):
        key_bytes = bytes(self.userOpenapiKey, 'utf-8')
        message = self.localUserId + '_'+ str(self.t)
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
        self.request_url += ('&userSecret={}&localUserId={}&t={}'.format(self.__get_api_signature(), self.localUserId, str(self.t)))
        print(self.request_url)

        api_response = requests.get(self.request_url, headers=self.headers, verify=False)
        return api_response


if __name__ == "__main__":

    localUserId = 'xxx'
    userOpenapiKey = 'xxx'

    app_id='3729de3c06'
    request_url = 'https://crashsight.qq.com/uniform/openapi/getSelectorDatas/appId/' + \
                  app_id + '/pid/1?types=version%2Cmember%2Cbundle%2Ctag%2Cchannel&fsn=477e4def-254f-405b-a3c5-7348b70fa5ed'
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)
    
