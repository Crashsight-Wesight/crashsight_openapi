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

        #  To get the current timestamp
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
    request_url = 'https://crashsight.qq.com/crashDoc/appId/' + \
                  app_id + '/platformId/10/crashHash/f7db4bd83071986fe75979431d3e3b95?fsn=d28d80a5-e41b-4c31-8ceb-1c695f740f54'
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)
