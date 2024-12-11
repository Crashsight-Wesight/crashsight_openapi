Crashsight OpenAPI 为崩溃/异常检测、报告、分析和解决方案提供专业数据服务接口，能够帮助开发人员更高效地定位和解决问题，不断提升产品的用户体验。

# CrashSight API 文档

## 调用环境

- **国内**: https://crashsight.qq.com
- **新加坡**: https://crashsight.wetest.net

## 接口使用说明
#### 部分接口需要做平台区分
**例如**:
- **安卓**: `/uniform/openapi/getCrashDeviceStat/platformId/1`
- **iOS**: `/uniform/openapi/getCrashDeviceStat/platformId/2`
- **PC**: `/uniform/openapi/getCrashDeviceStat/platformId/10`


## 签名和限制

### 公共请求参数

#### 1.1 URL 签名参数

| 参数 | 类型 | 是否必须 | 描述 |
| ---- | ---- | --------- | ----------- |
| t | int | Yes |  当前UNIX时间戳（单位是秒）|
| userSecret | String | Yes | 签名. 具体见签名算法. |
| localUserId | String | Yes | UserID |

#### 1.2 通用Header参数

| 参数 | 是否必须 | 描述 |
| ---- | --------- | ----------- |
| Content-Type | Yes | application/json |
| Accept-Encoding | Yes | \* |

#### 1.3 签名算法

localUserId：用户ID，可在账户管理里获取.\
![企业微信截图_16937999612475.png](https://data.eolink.com/ENGqJLJ6feb91e37022b13085117d4cb342b0bc78087c33)
user\_key：用户的OpenAPIKey，可在账户管理->OpenAPI秘钥管理里获取，如：bec5b56d-7ae7-43f7-8763-51580aed5fa2
![企业微信截图_16938002196859.png](https://data.eolink.com/h9pldCab2a138f87a6f8f5166d94a119749338822823483)
t: 当前时间戳（单位是秒），如：1618199626

### 程序

```
base64.b64encode(bytes(hmac.new(bytes(self.user_key, 'utf-8'), bytes(str(self.local_user_id) + '_' + str(self.t), 'utf-8'), digestmod=hashlib.sha256).hexdigest(), encoding=utf8))
```

以下方法用于访问请求:

1. 使用请求参数构建标准化Query String.
    ```
    message = localUserId + '_' + t
    key = userOpenapiKey
    base64_encode(hash_hmac('sha256', message, key, false));
    ```
2. 根据Base64编码规则将HMAC值编码为字符串，即可获得签名值 (Signature).
3. 添加获得的签名值作为Signature参数添加到请求参数中。请求签名过程完成。example:&userSecret=ODAxZGE1NmI3NDQ5Nzk0YjEzMjI1ZjJlZGY4NWNmZGE5Mzc4NGZmYjYzMjg4N2M0ODliMTkyZGU0MzBjODdkMw==&localUserId=12453&t=1693818679.
https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/signature.py

### 错误码

鉴权结果：
AuthenticationFailed
/* 身份鉴定失败，同时HTTP status code为401 /
Forbidden
/* 缺少权限，无权访问，同时HTTP status code为403 /


![企业微信截图_16945729271867.png](https://api.apifox.cn/api/v1/projects/3281673/resources/400048/image-preview)


## 通用字段说明

### 1. `appid`

- **获取方式**: 
  1. 首先需要加入项目组并获取相应权限。
  2. 在设置 -> 产品信息 -> appID 处获取。


![image.png](https://api.apifox.com/api/v1/projects/3856890/resources/481135/image-preview)

### 2. `localUserId`

- **获取方式**: 
  1. 右上角点击个人设置。
  2. 进入基础信息 -> 用户ID。


![image.png](https://api.apifox.com/api/v1/projects/3856890/resources/481136/image-preview)

### 3. `user_key`

- **获取方式**: 
  1. 右上角点击个人设置。
  2. 进入 OpenApi 密钥管理 -> 你的 OpenAPI 密钥。

  ![user_key 获取方式](https://api.apifox.com/api/v1/projects/3856890/resources/474645/image-preview)



## API 站点

需要根据用户注册地区访问不同的网站：
国内站点： https://crashsight.qq.com/uniform/
海外站点： https://crashsight.wetest.net/uniform/
