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
    def __init__(self,localUserId, userOpenapiKey, request_url, body):
        self.localUserId = localUserId
        self.headers = {
            'Content-Type': 'application/json',
            'Accept-Encoding':'*'
        }
        self.userOpenapiKey = userOpenapiKey
        self.request_url = request_url
        self.body = body
        self.localUserId = localUserId

        # To get the current timestamp
        self.t = int(time.time())

    """
        To calculate a signature value
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
        To get the API response
    """
    def do_post_request(self):
        # print(self.request_url)
        self.request_url += ('?userSecret={}&localUserId={}&t={}'.format(self.__get_api_signature(), self.localUserId, str(self.t)))
        print(self.request_url)
        api_response = requests.post(self.request_url, data = json.dumps(self.body), headers = self.headers)
        return api_response



if __name__ == "__main__":
    # 请根据OPEN_API的文档说明，以及所在的运行环境正确填写x_token, app_id, app_key以及request_url
    localUserId = 'xxx'
    userOpenapiKey = 'xxx'
    request_url = 'https://crashsight.qq.com/uniform/openapi/queryAccessList'
    
    body = {"uploadTimeBeginMillis":1701757736151,"deviceIdList":["PyQ4c3MD55tgowUv"],"appId":"3729de3c06","platformId":1,"skipDistinctQuery":True,"pageNumber":1,"pageSize":3000}
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)


    body = {"uploadTimeBeginMillis":1701761693003,"userIdList":["YQWUOpt"],"appId":"3729de3c06","platformId":1,"skipDistinctQuery":True,"pageNumber":1,"pageSize":3000}
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)
