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
    def __init__(self, x_token,app_id, app_key, request_url,body):
        self.x_token = x_token
        self.headers = {
            'Content-Type': 'application/json',
            'X-token': x_token,
            'Accept-Encoding': '*'
        }
        self.app_key = app_key
        self.request_url = request_url
        self.body=body
        self.app_id = app_id

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
    def do_post_request(self):
        # print(self.request_url)
        self.request_url += ('?appSecret={}&appId={}&t={}'.format(self.__get_api_signature(), self.app_id, str(self.t)))
        print(self.request_url)
        
        api_response = requests.post(self.request_url, data = json.dumps(self.body), headers = self.headers)
        return api_response

    def do_get_request(self):
        self.request_url += ('&appSecret={}&appId={}&t={}'.format(self.__get_api_signature(), self.app_id, str(self.t)))
        print(self.request_url)

        api_response = requests.get(self.request_url, headers=self.headers, verify=False)
        return api_response


if __name__ == "__main__":
    # 请根据OPEN_API的文档说明，以及所在的运行环境正确填写x_token, app_id, app_key以及request_url

    #新加坡环境
    x_token = 'xxx'
    app_id = 'xxx'
    app_key = 'xxx'
    request_url = 'https://crashsight.wetest.net/uniform/openapi/getCrashDeviceInfoByExpUid/platformId/1'
    #批量expUid请求获取机型deviceId
    body = {"requestid":"4f395abb53e82a1e1f57c7c86feb4cc4","stime":"2022-08-30 00:00:00","etime":"2022-08-31 00:00:00","type":"pretty","filters":{"expUid":["2f95d94c-824a-4fb3-8316-8a369fd52f09"]}}
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(x_token,app_id,  app_key, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)

    #批量deviceId请求获取崩溃列表
    request_url = 'https://crashsight.wetest.net/uniform/openapi/getCrashDeviceStat/platformId/1'
    body = {"requestid":"4f395abb53e82a1e1f57c7c86feb4cc4","stime":"2022-08-30 00:00:00","etime":"2022-08-31 00:00:00","type":"pretty","filters":{"deviceId":["37138989-52b1-4bcb-8bc2-b750270a1e6c"]}}

    crashsight_open_api_obj = crashsightOpenApi(x_token,app_id,  app_key, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)


    #根据crashId请求获取崩溃详情
    request_url = 'https://crashsight.wetest.net/uniform/openapi/crashDoc/appId/' + \
                  app_id + '/platformId/1/crashHash/F8:E9:EF:C1:25:93:70:1F:6F:0B:DC:DB:50:0D:89:65?fsn=a322bb8c-df92-460ca53d-053838b9e08'

    crashsight_open_api_obj = crashsightOpenApi(x_token, app_id, app_key, request_url,body)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)


    #国内环境
    x_token = 'xxx'
    app_id = 'xxx'
    app_key = 'xxx'
    request_url = 'https://crashsight.qq.com/uniform/openapi/getCrashDeviceInfoByExpUid/platformId/1'
    #批量expUid请求获取机型deviceId
    body = {"requestid":"4f395abb53e82a1e1f57c7c86feb4cc4","stime":"2022-08-30 00:00:00","etime":"2022-08-31 00:00:00","type":"pretty","filters":{"expUid":["f3be664b-8bf9-4c2a-9912-fb729228ecfd"]}}
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(x_token,app_id,  app_key, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)

    #批量deviceId请求获取崩溃列表
    request_url = 'https://crashsight.qq.com/uniform/openapi/getCrashDeviceStat/platformId/1'
    body = {"requestid":"4f395abb53e82a1e1f57c7c86feb4cc4","stime":"2022-08-30 00:00:00","etime":"2022-08-31 00:00:00","type":"pretty","filters":{"deviceId":["37138989-52b1-4bcb-8bc2-b750270a1e6c"]}}

    crashsight_open_api_obj = crashsightOpenApi(x_token,app_id,  app_key, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)


    #根据crashId请求获取崩溃详情
    request_url = 'https://crashsight.qq.com/uniform/openapi/crashDoc/appId/' + \
                  app_id + '/platformId/1/crashHash/85:AB:15:9D:AE:FF:F6:0F:51:68:55:16:71:6C:EF:1A?fsn=a322bb8c-df92-460ca53d-053838b9e08'

    crashsight_open_api_obj = crashsightOpenApi(x_token, app_id, app_key, request_url,body)
    result = crashsight_open_api_obj.do_get_request()
    print(result.content)

    


    
