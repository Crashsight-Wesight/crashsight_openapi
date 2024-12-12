# coding: utf-8
import requests
import time
import base64
import hmac
import hashlib
import urllib3

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

        # To get the current timestamp
        self.t = int(time.time())

    """
        To calculate a signature value
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
        To get the API response
    """
    def do_get_request(self):
        self.request_url += ('&appSecret={}&appId={}&t={}'.format(self.__get_api_signature(), self.app_id, str(self.t)))
        print(self.request_url)

        api_response = requests.get(self.request_url, headers=self.headers, verify=False)
        return api_response


if __name__ == "__main__":
    # Please follow the OpenAPI documentation and fill in the x_token, app_id, app_key and request_url correctly based on the runtime environment.
    x_token = 'xxx'
    app_id = 'xxx'
    app_key = 'xxx'
    #The domestic and overseas addresses are different; switch according to the requirements.
    request_url = 'https://crashsight.qq.com/uniform/openapi/crashList/crashDataType/undefined?start=0&searchType=detail&exceptionTypeList=Crash%2CNative%2CExtensionCrash&pid=1&platformId=1&issueId=650C2C6DF962E9D6ACE6BF5C9F27676D&rows=50&appId=3729de3c06&fsn=a59681f5-6848-479f-92a1-8f6602b62970'
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(x_token, app_id, app_key, request_url)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)
