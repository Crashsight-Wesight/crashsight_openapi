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
    # 请根据OPEN_API的文档说明，以及所在的运行环境正确填写x_token, app_id, app_key以及request_url

    # OPEN_API文档样例参数样例：
    # x_token = 'F3108EBF-2AFB-459C-87A9-DEEAB2F54882'
    # app_id = '3729de3c06'
    # app_key = 'd8dff3bd-4841-48aa-8503-cd949c4894ce'
    # request_url = 'https://crashsight.qq.com/getTopIssue/appId/' + \
    #                app_id + '/platformId/1/version/-1/date/20210810/type' + \
    #               '/crash/limit/20/topIssueDataType/unSystemExit?fsn=4d8a5f7f-935e-4d7a-be35-d4edb2424fb5'
    # print(request_url)

    # STAGING环境参数样例：Pre-suziefu-test项目
    localUserId = 'xxx'
    userOpenapiKey = 'xxx'
    app_id = '53a4ffeb78'
    request_url = 'https://crashsight.qq.com/crashDoc/appId/' + \
                  app_id + '/platformId/10/crashHash/f7db4bd83071986fe75979431d3e3b95?fsn=d28d80a5-e41b-4c31-8ceb-1c695f740f54'
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)
