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
    def do_get_request(self):
        self.request_url += ('&userSecret={}&localUserId={}&t={}'.format(self.__get_api_signature(), self.localUserId, str(self.t)))
        print(self.request_url)

        api_response = requests.get(self.request_url, headers=self.headers, verify=False)
        return api_response


if __name__ == "__main__":
    # Please follow the OpenAPI documentation and fill in the localUserId, userOpenapiKey, and request_url correctly based on the runtime environment.

    localUserId = 'xxx'
    userOpenapiKey = 'xxx'
    app_id = 'xxx'
    #The domestic and overseas addresses are different; switch according to the requirements.
    request_url = 'https://crashsight.qq.com/uniform/openapi/crashDoc/appId/' + \
                  app_id + '/platformId/1/crashHash/6D:EE:9C:AF:EB:91:DA:EC:2D:AD:AA:7B:06:94:7D:52?fsn=a322bb8c-df92-460ca53d-053838b9e08'
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)
