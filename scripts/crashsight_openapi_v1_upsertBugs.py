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
    def do_post_request(self):
        # print(self.request_url)
        self.request_url += ('?userSecret={}&localUserId={}&t={}'.format(self.__get_api_signature(), self.localUserId, str(self.t)))
        print(self.request_url)
        api_response = requests.post(self.request_url, data = json.dumps(self.body), headers = self.headers)
        return api_response


if __name__ == "__main__":

    # 请根据OPEN_API的文档说明，以及所在的运行环境正确填写app_id, localUserId, userOpenapiKey以及request_url

    localUserId = 'xxx'
    userOpenapiKey = 'yyy'

    #国内和海外地址不同，根据需求进行切换
    request_url =  'https://crashsight.qq.com/uniform/openapi/upsertBugs'
    #
    body = {"appId":"d98b9f7eec","platformId":1,"issueList":[{"issueHash":"7A5DD858AC3CF6CBD437DE7F3B6703F4","bugInfoList":[{"status":"new","title":"【CrashSight一键提单】java.lang.RuntimeException -  - 2023-08-25 14:45:39","description":"异常Issue ID: 7A5DD858AC3CF6CBD437DE7F3B6703F4\n<br><br>\n异常详情地址: <a href='https://crashsight.wetest.net/crash-reporting/crashes/d98b9f7eec/7A5DD858AC3CF6CBD437DE7F3B6703F4/7A5DD858AC3CF6CBD437DE7F3B6703F4/report-id/CDB2BFF4C44142FFA9A8DE47B5868CEC?pid=1'>https://crashsight.wetest.net/crash-reporting/crashes/d98b9f7eec/7A5DD858AC3CF6CBD437DE7F3B6703F4/7A5DD858AC3CF6CBD437DE7F3B6703F4/report-id/CDB2BFF4C44142FFA9A8DE47B5868CEC?pid=1</a>\n<br><br>\n最近上报时间: 2023-08-25 14:45:39 223\n<br><br>\n异常进程#线程: com.tencent.demo#Thread-221(221)\n<br><br>\n异常消息：sNSXTvFGp6ZGrorljP6WPxsGtKc5px\n<br><br>\n出错堆栈:\n<br><pre>irgMyesZayrR</pre>\n<br><br>\n发生时间: 2020-05-07 18:36:48<br>\n上报时间: 2023-08-25 14:45:39<br>\n应用包名: com.tencent.demo<br>\n应用版本: 1.0.3<br>\n设备机型: 魅族 M6<br>\n系统版本: Android 4.4.2,level 20<br>\n发生次数：763670<br>\n影响设备数：762282<br>\n","reporter":"anguswang","includeAttachments":false,"attachmentFilenameList":[],"severity":"serious","versionReport":"发现版本2","iterationId":"1020428185001284771","releaseId":"1020428185000072689","rawValueCurrentOwner":["v_fzqfang"],"currentOwner":"v_fzqfang"}]}]}


    crashsight_open_api_obj = crashsightOpenApi(localUserId,  userOpenapiKey, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)
