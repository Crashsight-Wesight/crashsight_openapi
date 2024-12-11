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
    # Please follow the OpenAPI documentation and fill in the localUserId, userOpenapiKey, and request_url correctly based on the runtime environment.


    localUserId = 'xxx'
    userOpenapiKey = 'xxx'
    
    #The domestic and overseas addresses are different; switch according to the requirements.
    request_url = 'https://crashsight.qq.com/uniform/openapi/getCrashDeviceInfo/platformId/2'
    #issueId request
    body = {"requestid":"4f395abb53e82a1e1f57c7c86feb4cc4","stime":"2023-12-01 00:00:00","etime":"2023-12-04 00:00:00","type":"pretty","appId":"9c8974bff2","filters":{"issueId":["3E04F25D48C8FF5CA38E276517C98D81"]},"limit":1000}
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)

    
