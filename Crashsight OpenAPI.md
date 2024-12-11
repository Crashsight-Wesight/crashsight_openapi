---
title: Crashsight OpenAPI 中文版
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# Crashsight OpenAPI 中文版

Base URLs:

# Authentication

# 鉴权

## POST Header参数

POST /Header参数

Header参数

采用HTTP Header传递公共参数

> Body 请求参数

```json
{
  "X-Gateway-RequestID": "",
  "X-Gateway-Stage": "",
  "X-Version": "",
  "Content-Type": "",
  "Accept-Encoding": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» X-Gateway-RequestID|body|string| 否 |请求ID，标记唯一请求，建议每次唯一。 - 如果客户端请求带有X-Gateway-RequestID字段，则使用客户端传来的id回复 - 如果没有系统会自动补充并返回|
|» X-Gateway-Stage|body|string| 否 |测试环境为TEST，预发布环境为PRE，正式环境为RELEASE 如不设置或设置为非指定字段，则认为访问正式环境 字段不区分大小写|
|» X-Version|body|string| 否 |测试环境为TEST，预发布环境为PRE，正式环境为RELEASE 如不设置或设置为非指定字段，则认为访问正式环境 字段不区分大小写|
|» Content-Type|body|string| 否 |application/json|
|» Accept-Encoding|body|string| 否 |*|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

# 概览统计

## POST 获取趋势数据(最近N天)(新鉴权)

POST /env/uniform/openapi/getTrendEx

获取趋势数据(最近N天)(新鉴权)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例： https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getTrendEx.py

> Body 请求参数

```json
{
  "appId": "4bd2da9ae1",
  "platformId": 1,
  "startDate": "20230605",
  "endDate": "20230704",
  "type": "crash",
  "fsn": "",
  "dataType": "trendData",
  "vm": 0,
  "versionList": [
    "8.4.1.1.804010199",
    "3.82.1.4"
  ],
  "needCountryDimension": false,
  "countryList": "[]",
  "mergeMultipleVersionsWithInaccurateResult": true
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 是 |none|
|Accept-Encoding|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |none|
|» platformId|body|integer| 是 |none|
|» startDate|body|string| 是 |none|
|» endDate|body|string| 是 |none|
|» type|body|string| 是 |none|
|» fsn|body|string| 是 |none|
|» dataType|body|string| 是 |none|
|» vm|body|integer| 是 |none|
|» versionList|body|[string]| 是 |none|
|» needCountryDimension|body|boolean| 是 |none|
|» countryList|body|string| 是 |none|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| 是 |none|
|» userSceneTagList|body|[string]| 是 |场景筛选（可选）|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "",
    "data": [
      {
        "appId": "4bd2da9ae1",
        "platformId": 1,
        "version": "MERGED",
        "date": "20230605",
        "type": "crash",
        "country": "-1",
        "crashNum": 0,
        "crashUser": 0,
        "reportNumAllData": 0,
        "reportDeviceAllData": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "4bd2da9ae1",
        "platformId": 1,
        "version": "MERGED",
        "date": "20230704",
        "country": "-1",
        "crashNum": 0,
        "crashUser": 0,
        "reportNumAllData": 0,
        "reportDeviceAllData": 0,
        "accessNum": 13,
        "accessUser": 1
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» country|string|true|none||国家|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» reportNumAllData|integer|true|none||none|
|» reportDeviceAllData|integer|true|none||none|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|

## POST  获取网络设备数据

POST /env/uniform/openapi/getNetworkDevices/platformId/1/**

获取趋势数据(最近N天)(新鉴权)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

安卓：{{env}}/uniform/openapi/getNetworkDevices/platformId/1/**
IOS：{{env}}/uniform/openapi/getNetworkDevices/platformId/2/**
以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例： https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getNetworkDevices.py

> Body 请求参数

```json
{
  "requestid": "test",
  "stime": "2024-10-22 17:02:08",
  "etime": "2024-10-23 17:02:08",
  "appId": "xxx"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 是 |none|
|Accept-Encoding|header|string| 是 |none|
|body|body|object| 否 |none|
|» requestid|body|string| 是 |none|
|» stime|body|string| 是 |none|
|» etime|body|string| 是 |none|
|» appId|body|string| 是 |none|
|» filters|body|object| 是 |按版本筛选（可选项）|
|»» productVersion|body|string| 是 |none|

> 返回示例

```json
{
  "requestid": "xxxx",
  "code": 200,
  "errmsg": null,
  "data": {
    "columns": [
      "dt",
      "model",
      "uploadIp",
      "name",
      "uniq(deviceId)",
      "uniq(userId)"
    ],
    "values": [
      [
        "2024-10-24 00:00:00",
        "iPhone16%252C1",
        "101.226.154.151",
        "name",
        1,
        2
      ]
    ],
    "results": null
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||none|
|» code|integer|true|none||none|
|» errmsg|null|true|none||none|
|» data|object|true|none||none|
|»» columns|[string]|true|none||none|
|»» values|[array]|true|none||none|

*oneOf*

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»»» *anonymous*|string|false|none||none|

*xor*

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»»» *anonymous*|integer|false|none||none|

*continued*

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|results|null|true|none||none|
|cost|integer|true|none||none|

## POST 获取崩溃、ANR、错误类型排行榜(影响设备数/设备崩溃率/联网设备数)

POST /env//uniform/openapi/fetchDimensionTopStats

崩溃、ANR、错误类型的排行榜接口(影响设备数/设备崩溃率/联网设备数)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_fetchDimensionTopStats.py

> Body 请求参数

```json
{
  "appId": "3729de3c06",
  "platformId": 1,
  "mergeMultipleVersionsWithInaccurateResult": false,
  "version": "-1",
  "minDate": "20231208",
  "maxDate": "20231208",
  "mergeMultipleDatesWithInaccurateResult": false,
  "type": "crash",
  "limit": 5,
  "field": "version",
  "sortByException": true,
  "countryList": [],
  "needCountryDimension": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 否 |none|
|Accept-Encoding|header|string| 否 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |项目ID|
|» platformId|body|integer| 是 |平台类型，安卓端：1，iOS端：2，PC端：10|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| 是 |多版本的结果是否要合并成一条结果。合并方式为所有单个版本的设备数、次数直接相加。|
|» version|body|string| 是 |版本。版本支持通配符|
|» minDate|body|string| 是 |开始时间 YYMMDD|
|» maxDate|body|string| 是 |结束时间 YYMMDD|
|» mergeMultipleDatesWithInaccurateResult|body|boolean| 是 |多天的结果是否要合并成一条。合并方式为所有单个版本的设备数、次数直接相加。|
|» type|body|string| 是 |三种类型-crash,anr,error|
|» limit|body|integer| 是 |条数限制|
|» field|body|string| 是 |聚合维度  设备：model 系统版本：osVersion 应用版本：version|
|» sortByException|body|boolean| 是 |排序标识|
|» countryList|body|[string]| 是 |如果设置了需要国家维度的统计，则传入需要查询的国家名称列表。如果设置了needCountryDimension但countryList为空数组，则表示查询全部国家地区|
|» needCountryDimension|body|string| 是 |true: 需要国家维度的统计 false: 不需要|

> 返回示例

```json
{
  "status": 200,
  "ret": 200,
  "data": [
    {
      "appId": "3729de3c06",
      "platformId": 1,
      "fieldValue": "1.0.3",
      "date": "20231208",
      "exceptionDevices": 2400,
      "accessDevices": 12010
    }
  ],
  "message": "OK",
  "errorCode": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|integer|true|none||none|
|» data|[object]|true|none||none|
|»» appId|string|false|none||产品id|
|»» platformId|integer|false|none||平台id|
|»» fieldValue|string|false|none||维度值|
|»» date|string|false|none||日期|
|»» exceptionDevices|integer|false|none||影响设备数|
|»» accessDevices|integer|false|none||联网设备数|
|» message|string|true|none||none|
|» errorCode|string|true|none||none|

## POST 获取趋势数据(最近N天)

POST /env//uniform/openapi/getTrend

获取趋势数据(最近N天)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getTrend.py

> Body 请求参数

```json
{
  "appId": "7786d1a114",
  "platformId": 1,
  "startDate": "20230630",
  "endDate": "20230706",
  "type": "crash",
  "fsn": "d655ff49-7efe-4cf8-9951-5012b379cb51",
  "dataType": "trendData",
  "vm": 0,
  "subModuleId": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 否 |none|
|Accept-Encoding|header|string| 否 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |产品id|
|» platformId|body|integer| 是 |平台类型，安卓端：1，iOS端：2，PC端：10|
|» startDate|body|string| 是 |开始时间 YYMMDD|
|» endDate|body|string| 是 |结束时间  YYMMDD|
|» type|body|string| 是 |三种类型-crash,anr,error|
|» fsn|body|string| 是 |fsn值可以写死|
|» dataType|body|string| 是 |trendData|
|» vm|body|integer| 是 |0 全量 1 真机 2 模拟器|
|» subModuleId|body|string| 是 |地图id|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "data": [
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "20210401",
        "type": "crash",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "20210402",
        "type": "crash",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "20210403",
        "type": "crash",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "20210404",
        "type": "crash",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "20210405",
        "type": "crash",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "20210406",
        "type": "crash",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "20210407",
        "type": "crash",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» type|string|true|none||类型|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|

## POST 获取分钟级崩溃数据（项目私有）

POST /env//uniform/openapi/getMinuteCrashData

获取趋势数据(最近N天)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getMinuteCrashData.py

> Body 请求参数

```json
{
  "appId": "xxxx",
  "stime": "2024-09-19 21:45:00",
  "etime": "2024-09-19 21:47:00",
  "product_version": "1.1.0.407071",
  "limit": 10
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 否 |none|
|Accept-Encoding|header|string| 否 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |none|
|» stime|body|string| 是 |none|
|» etime|body|string| 是 |none|
|» product_version|body|string| 是 |none|
|» limit|body|integer| 是 |none|

> 返回示例

```json
{
  "requestid": null,
  "code": 200,
  "errmsg": null,
  "data": {
    "columns": [
      "dt",
      "app_id",
      "crash_device",
      "access_device"
    ],
    "values": [
      [
        "2024-09-19 21:49:00",
        "1106467070",
        1,
        316
      ],
      [
        "2024-09-19 21:47:00",
        "1106467070",
        138,
        74253
      ],
      [
        "2024-09-19 21:48:00",
        "1106467070",
        129,
        66120
      ],
      [
        "2024-09-19 21:45:00",
        "1106467070",
        147,
        76424
      ],
      [
        "2024-09-19 21:46:00",
        "1106467070",
        169,
        75224
      ]
    ],
    "results": null
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## GET 获取趋势数据(今天-累计)

GET /env/uniform/openapi/getAppRealTimeTrendAppend

获取趋势数据(今天-累计)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getAppRealTimeTrendAppend.py

> Body 请求参数

```json
{
  "appId": "7786d1a114",
  "platformId": 1,
  "startHour": "2020060400",
  "endHour": "2020060423",
  "type": "crash",
  "fsn": "7ff02834-2c46-49eb-a825-99d374388765",
  "version": "2.7.5.-1",
  "dataType": "realTimeTrendData",
  "vm": 0
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» appId|body|string| 是 |none|
|» platformId|body|integer| 是 |none|
|» startHour|body|string| 是 |none|
|» endHour|body|string| 是 |none|
|» type|body|string| 是 |多种类型-crash,anr,error,oom|
|» fsn|body|string| 是 |none|
|» version|body|string| 是 |none|
|» dataType|body|string| 是 |none|
|» vm|body|integer| 是 |none|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "data": [
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040800",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040801",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040802",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040803",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040804",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040805",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040806",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040807",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040808",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040809",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040810",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040811",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040812",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040813",
        "crashNum": 132,
        "crashUser": 60,
        "accessNum": 141249,
        "accessUser": 115041
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040814",
        "crashNum": 338,
        "crashUser": 163,
        "accessNum": 363494,
        "accessUser": 276739
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040815",
        "crashNum": 610,
        "crashUser": 297,
        "accessNum": 615874,
        "accessUser": 442173
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040816",
        "crashNum": 872,
        "crashUser": 425,
        "accessNum": 900313,
        "accessUser": 621881
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040817",
        "crashNum": 1122,
        "crashUser": 546,
        "accessNum": 1202687,
        "accessUser": 800755
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040818",
        "crashNum": 1386,
        "crashUser": 673,
        "accessNum": 1524840,
        "accessUser": 986791
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040819",
        "crashNum": 1538,
        "crashUser": 748,
        "accessNum": 1692083,
        "accessUser": 1076518
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|

## GET 获取趋势数据(小时粒度)

GET /env/uniform/openapi/getRealTimeHourlyStat

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getRealTimeHourlyStat.py

> Body 请求参数

```json
{
  "appId": "",
  "platformId": 0,
  "version": "",
  "versionList": "",
  "startHour": "",
  "endHour": "",
  "type": "",
  "fsn": "",
  "dataType": "",
  "vm": 0,
  "needCountryDimension": false,
  "countryList": "",
  "mergeMultipleVersionsWithInaccurateResult": false
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» appId|body|string| 是 |产品id|
|» platformId|body|integer| 是 |平台类型，安卓端：1，iOS端：2，PC端：10|
|» version|body|string| 是 |默认全版本，-1|
|» versionList|body|string| 是 |如果需要查询多版本，使用versionList。这时候不需要填写version字段|
|» startHour|body|string| 是 |开始时间YYMMDDHH|
|» endHour|body|string| 是 |结束时间YYMMDDHH|
|» type|body|string| 是 |多种类型-crash,anr,error,oom|
|» fsn|body|string| 是 |fsn值可以写死|
|» dataType|body|string| 是 |realTimeTrendData|
|» vm|body|integer| 是 |0全量1真机2模拟器|
|» needCountryDimension|body|boolean| 是 |true: 需要国家维度的统计 false: 不需要|
|» countryList|body|string| 是 |如果设置了需要国家维度的统计，则传入需要查询的国家名称列表。如果设置了needCountryDimension但countryList为空数组，则表示查询全部国家地区|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| 是 |多版本的结果是否要合并。|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "data": [
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040800",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040801",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040802",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040803",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040804",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040805",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040806",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040807",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040808",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040809",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040810",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040811",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040812",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040813",
        "crashNum": 132,
        "crashUser": 60,
        "accessNum": 141437,
        "accessUser": 115178
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040814",
        "crashNum": 206,
        "crashUser": 103,
        "accessNum": 222255,
        "accessUser": 176102
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040815",
        "crashNum": 276,
        "crashUser": 136,
        "accessNum": 254699,
        "accessUser": 200096
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040816",
        "crashNum": 258,
        "crashUser": 126,
        "accessNum": 282389,
        "accessUser": 221376
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040817",
        "crashNum": 252,
        "crashUser": 123,
        "accessNum": 302455,
        "accessUser": 238038
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040818",
        "crashNum": 40,
        "crashUser": 20,
        "accessNum": 52130,
        "accessUser": 45962
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|

## POST 获取小时级TOP问题列表

POST /env/uniform/openapi/getTopIssueHourly

小时级TOP问题列表

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/openapi/crashsight_openapi_v1_getTopIssueHourly.py

> Body 请求参数

```json
{
  "appId": "d98b9f7eec",
  "platformId": 1,
  "version": "-1",
  "startHour": "2022101404",
  "type": "crash",
  "limit": 5,
  "topIssueDataType": "",
  "needCountryDimension": true,
  "countryList": [
    "中国"
  ],
  "fsn": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 否 |none|
|Accept-Encoding|header|string| 否 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |产品id|
|» platformId|body|integer| 是 |平台id|
|» version|body|string| 是 |项目版本,-1代表全版本|
|» startHour|body|string| 是 |开始时间 YYMMDDHH|
|» type|body|string| 是 |三种类型-crash,anr,error|
|» limit|body|integer| 是 |行数限制，获取多少行|
|» topIssueDataType|body|string| 是 |行数限制，获取多少行|
|» needCountryDimension|body|boolean| 是 |是否需要过滤出特定国家下的top问题。 true: 获取指定国家下的TOP问题 false: 获取不区分地区的TOP问题|
|» countryList|body|[string]| 是 |只有在needCountryDimension为true时才生效，指定需要过滤的国家列表。|
|» fsn|body|string| 是 |fsn值可以写死，如上所示|

> 返回示例

```json
{
  "versionCrashUser": 200,
  "preDayVersionCrashUser": 200,
  "topIssueList": [
    {
      "appId": "d98b9f7eec",
      "platformId": 1,
      "version": -1,
      "date": "",
      "type": "",
      "issueId": "B0B0C7EAFEF684F2ACCA492E2F194760",
      "firstUploadTime": "2021-01-13 14:22:00 671",
      "firstUploadTimestamp": 0,
      "crashUser": 45,
      "crashNum": 45,
      "accumulateCrashNum": 511153,
      "accumulateCrashUser": 510012,
      "state": 2,
      "processors": "100006203",
      "exceptionName": "java.lang.RuntimeException",
      "exceptionMessage": "yyY9Wfe9uXCw6lgPTmpZ2SECbHoQXT",
      "keyStack": "",
      "lastUpdateTime": "2022-10-14 11:54:02 132",
      "lastUpdateTimestamp": 0,
      "issueVersions": [
        {
          "version": "1.0.3",
          "firstUploadTimestamp": 0,
          "lastUploadTimestamp": 0,
          "count": 0,
          "deviceCount": 0,
          "systemExitCount": 0,
          "systemExitDeviceCount": 0
        }
      ],
      "preDayCrashUser": 36,
      "preDayCrashNum": 36,
      "prevHourCrashDevices": 27,
      "tags": [],
      "is_system_exit": false
    }
  ],
  "crashDevices": 200,
  "prevHourCrashDevices": 200,
  "prevDaySameHourCrashDevices": 200,
  "accessDevices": 1000,
  "prevHourAccessDevices": 1000,
  "prevDaySameHourAccessDevices": 1000
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» versionCrashUser|integer|true|none||影响设备数量|
|» preDayVersionCrashUser|integer|true|none||前一天影响设备数量|
|» topIssueList|[object]|true|none||none|
|»» appId|string|false|none||产品id|
|»» platformId|integer|false|none||平台id|
|»» version|integer|false|none||项目版本|
|»» date|string|false|none||时间|
|»» type|string|false|none||类型|
|»» issueId|string|false|none||问题issueId|
|»» firstUploadTime|string|false|none||首次上报时间|
|»» firstUploadTimestamp|integer|false|none||none|
|»» crashUser|integer|false|none||影响设备数|
|»» crashNum|integer|false|none||发生次数|
|»» accumulateCrashNum|integer|false|none||累计影响次数|
|»» accumulateCrashUser|integer|false|none||累计影响设备|
|»» state|integer|false|none||处理状态|
|»» processors|string|false|none||处理人|
|»» exceptionName|string|false|none||异常类型|
|»» exceptionMessage|string|false|none||异常信息|
|»» keyStack|string|false|none||堆栈信息|
|»» lastUpdateTime|string|false|none||最近更新时间|
|»» lastUpdateTimestamp|integer|false|none||none|
|»» issueVersions|[object]|false|none||issue版本集合|
|»»» version|string|false|none||none|
|»»» firstUploadTimestamp|integer|false|none||none|
|»»» lastUploadTimestamp|integer|false|none||none|
|»»» count|integer|false|none||none|
|»»» deviceCount|integer|false|none||none|
|»»» systemExitCount|integer|false|none||none|
|»»» systemExitDeviceCount|integer|false|none||none|
|»» preDayCrashUser|integer|false|none||none|
|»» preDayCrashNum|integer|false|none||none|
|»» prevHourCrashDevices|integer|false|none||none|
|»» tags|[string]|false|none||none|
|»» is_system_exit|boolean|false|none||none|
|» crashDevices|integer|true|none||none|
|» prevHourCrashDevices|integer|true|none||none|
|» prevDaySameHourCrashDevices|integer|true|none||none|
|» accessDevices|integer|true|none||none|
|» prevHourAccessDevices|integer|true|none||none|
|» prevDaySameHourAccessDevices|integer|true|none||none|

## GET 获取当日异常累计数据：崩溃，ANR，卡顿，错误

GET /uniform/openapi/getRealTimeAppendStat

获取查询日异常累计数据：崩溃，ANR，卡顿，错误

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getRealTimeAppendStat.py

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|appId|query|string| 是 |产品id|
|platformId|query|string| 是 |平台id,1是安卓,2是ios|
|startHour|query|string| 是 |格式YYYYMMDDHH，小时的部分必须是00|
|endHour|query|string| 是 |格式YYYYMMDDHH，必须和startHour是同一天|
|type|query|string| 是 |三种类型-crash,anr,error|
|fsn|query|string| 否 |fsn值可以写死或者自动生成|

#### 枚举值

|属性|值|
|---|---|
|platformId|1|
|platformId|2|
|platformId|10|
|type|crash|
|type|anr|
|type|error|

> 返回示例

```json
{
  "appId": "a48e55df8b",
  "platformId": 2,
  "version": "-1",
  "date": "2021040818",
  "type": "",
  "accessNum": 1255365,
  "accessUser": 832770,
  "crashNum": 1164,
  "crashUser": 566,
  "anrNum": 0,
  "anrUser": 0,
  "errorNum": 67962,
  "errorUser": 33322,
  "vmCrashNum": 0,
  "vmCrashUser": 0,
  "vmAnrNum": 0,
  "vmAnrUser": 0,
  "vmErrorNum": 0,
  "vmErrorUser": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» type|string|true|none||类型|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» anrNum|integer|true|none||卡顿次数|
|» anrUser|integer|true|none||卡顿用户数|
|» errorNum|integer|true|none||错误次数|
|» errorUser|integer|true|none||错误用户数|
|» vmCrashNum|integer|true|none||模拟器崩溃次数|
|» vmCrashUser|integer|true|none||模拟器崩溃用户数|
|» vmAnrNum|integer|true|none||模拟器卡顿次数|
|» vmAnrUser|integer|true|none||模拟器卡顿用户数|
|» vmErrorNum|integer|true|none||模拟器错误次数|
|» vmErrorUser|integer|true|none||模拟器错误用户数|

## POST 获取当日异常累计数据：崩溃，ANR，卡顿，错误

POST /uniform/openapi/getRealTimeAppendStat

> Body 请求参数

```json
{
  "appId": "string",
  "platformId": "1",
  "startHour": "string",
  "endHour": "string",
  "type": "crash",
  "fsn": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» appId|body|string| 是 |产品id|
|» platformId|body|string| 是 |平台id,1是安卓,2是ios|
|» startHour|body|string| 否 |格式YYYYMMDDHH，小时的部分必须是00|
|» endHour|body|string| 否 |格式YYYYMMDDHH，必须和startHour是同一天|
|» type|body|string| 否 |三种类型-crash,anr,error|
|» fsn|body|string| 是 |fsn值可以写死或者自动生成|

#### 枚举值

|属性|值|
|---|---|
|» platformId|1|
|» platformId|2|
|» platformId|10|
|» type|crash|
|» type|anr|
|» type|error|

> 返回示例

> 200 Response

```json
{
  "appId": "string",
  "platformId": 0,
  "version": "string",
  "date": "string",
  "type": "string",
  "accessNum": 0,
  "accessUser": 0,
  "crashNum": 0,
  "crashUser": 0,
  "anrNum": 0,
  "anrUser": 0,
  "errorNum": 0,
  "errorUser": 0,
  "vmCrashNum": 0,
  "vmCrashUser": 0,
  "vmAnrNum": 0,
  "vmAnrUser": 0,
  "vmErrorNum": 0,
  "vmErrorUser": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» type|string|true|none||类型|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» anrNum|integer|true|none||卡顿次数|
|» anrUser|integer|true|none||卡顿用户数|
|» errorNum|integer|true|none||错误次数|
|» errorUser|integer|true|none||错误用户数|
|» vmCrashNum|integer|true|none||模拟器崩溃次数|
|» vmCrashUser|integer|true|none||模拟器崩溃用户数|
|» vmAnrNum|integer|true|none||模拟器卡顿次数|
|» vmAnrUser|integer|true|none||模拟器卡顿用户数|
|» vmErrorNum|integer|true|none||模拟器错误次数|
|» vmErrorUser|integer|true|none||模拟器错误用户数|

# 异常分析

## POST 崩溃分析自定义检索

POST /env/uniform/openapi/advancedSearchEx

获取趋势数据(今天-累计)(新鉴权)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

> Body 请求参数

```json
{
  "appId": "7786d1a114",
  "platformId": 1,
  "startHour": "2020060400",
  "endHour": "2020060423",
  "type": "crash",
  "fsn": "7ff02834-2c46-49eb-a825-99d374388765",
  "version": "2.7.5.-1",
  "dataType": "realTimeTrendData",
  "vm": 0
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 否 |none|
|Accept-Encoding|header|string| 否 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |产品id|
|» platformId|body|integer| 是 |平台id|
|» startHour|body|string| 是 |开始时间 YYMMDDHH|
|» endHour|body|string| 是 |结束时间 YYMMDDHH|
|» type|body|string| 是 |三种类型-crash,anr,error|
|» fsn|body|string| 是 |fsn值可以写死|
|» version|body|string| 是 |-1代表全版本|
|» dataType|body|string| 是 |realTimeTrendData|
|» vm|body|integer| 是 |0 全量 1 真机 2 模拟器|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "data": [
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040800",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040801",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040802",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040803",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040804",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040805",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040806",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040807",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040808",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040809",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040810",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040811",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040812",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040813",
        "crashNum": 132,
        "crashUser": 60,
        "accessNum": 141249,
        "accessUser": 115041
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040814",
        "crashNum": 338,
        "crashUser": 163,
        "accessNum": 363494,
        "accessUser": 276739
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040815",
        "crashNum": 610,
        "crashUser": 297,
        "accessNum": 615874,
        "accessUser": 442173
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040816",
        "crashNum": 872,
        "crashUser": 425,
        "accessNum": 900313,
        "accessUser": 621881
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040817",
        "crashNum": 1122,
        "crashUser": 546,
        "accessNum": 1202687,
        "accessUser": 800755
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040818",
        "crashNum": 1386,
        "crashUser": 673,
        "accessNum": 1524840,
        "accessUser": 986791
      },
      {
        "appId": "a48e55df8b",
        "platformId": 2,
        "version": "-1",
        "date": "2021040819",
        "crashNum": 1538,
        "crashUser": 748,
        "accessNum": 1692083,
        "accessUser": 1076518
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|

## POST 获取崩溃详情(支持PC)

POST /env/uniform/openapi/crashDoc

> Body 请求参数

```json
{
  "appId": "string",
  "platformId": "string",
  "crashHash": "string",
  "fsn": "string",
  "logtype": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» appId|body|string| 是 |none|
|» platformId|body|string| 是 |none|
|» crashHash|body|string| 是 |none|
|» fsn|body|string| 是 |none|
|» logtype|body|string| 是 |none|

> 返回示例

```json
{
  "statusCode": 0,
  "message": "null",
  "reqSendTimestamp": 0,
  "rspReceivedTimestamp": 0,
  "rspSendTimestamp": 0,
  "numFound": 0,
  "crashMap": {
    "id": "D8:CA:9E:C4:4F:55:56:E8:2A:01:8B:0B:8A:4C:01:F0",
    "issueId": "4273DBD3409C2783706F3F15E140F25A",
    "productVersion": "3.2.5",
    "model": "魅族 M8",
    "userId": "Sumxc4c",
    "expMessage": "sNSXTvFGp6ZGrorljP6WPxsGtKc5px",
    "type": "100",
    "processName": "com.tencent.crashsight.demo.crashsightqq",
    "retraceStatus": -3,
    "uploadTime": "2021-04-09T12:21:25.663+0000",
    "uploadTimestamp": 1617970885663,
    "crashTime": "2020-05-07T10:36:48.991+0000",
    "crashTimestamp": 1588847808991,
    "mergeVersion": "11",
    "messageVersion": "2",
    "isSystemStack": 1,
    "rqdUuid": "b1099c1d-41d8-4b44-89e4-ec67bb3dbdf4",
    "retraceResult": "1_0_2_0_0_0_0_9_0",
    "appInBack": "false",
    "cpuType": "x86",
    "subVersionIssueId": "5D7A43A93A533F0A06D4F2C5A8F2CEEF",
    "crashId": "D8CA9EC44F5556E82A018B0B8A4C01F0",
    "bundleId": "com.tencent.crashsight.demo.crashsightqq",
    "sdkVersion": "3.1.7(1.6.0)-3.7.1",
    "osVer": "Android 4.4.2,level 16",
    "expAddr": "com.tencent.crashsight.demo.MainActivity$11$2.run(MainActivity.java:529)",
    "threadName": "Thread-221(221)",
    "memSize": "1587986432",
    "diskSize": "33999818752",
    "imei": "null",
    "imsi": "null",
    "cpuName": "fail",
    "brand": "samsung",
    "freeMem": "1168867328",
    "freeStorage": "31347867648",
    "freeSdCard": "31347867648",
    "mac": "null",
    "country": "CN",
    "totalSD": "33999818752",
    "channelId": "testchannel",
    "startTime": "1588837884696",
    "startTimestamp": 1588837884696,
    "callStack": "irgMyesZayrR",
    "retraceCrashDetail": "irgMyesZayrR",
    "buildNumber": "samsung",
    "rom": "fail%2Ffail",
    "retraceTimestamp": 0,
    "apn": "WIFI",
    "appInAppstore": false,
    "expName": "java.lang.RuntimeException",
    "deviceId": "hx6DLV78mm9ChnvC",
    "crashCount": 0,
    "isRooted": "true",
    "isVirtualMachine": 320,
    "modelOriginalName": "魅族 M8"
  },
  "detailMap": {
    "attatchCount": 0,
    "quaInner": "null",
    "appInfo": "null",
    "stackName": "FileObserver(202);main(1);FinalizerWatchdogDaemon(191);crashsightThread-1(200);OkHttp ConnectionPool(219);Signal Catcher(187);AsyncTask #3(196);Binder_2(193);crashsightThread-2(201);JDWP(188);AsyncTask #2(195);FinalizerDaemon(190);ReferenceQueueDaemon(189);crashsightThread-3(203);java.lang.ProcessManager(206);Thread-220(220);Binder_3(207);Binder_1(192);AsyncTask #1(194);GC(186);",
    "excepitonAddress": "null",
    "retraceCrashDetail": "irgMyesZayrR",
    "freeMem": 0,
    "appBaseAddr": "null",
    "battery": 0,
    "now": "null",
    "archVersion": "null",
    "attachName": "valueMapOthers.txt;log.txt;",
    "tel": "null",
    "id": "D8:CA:9E:C4:4F:55:56:E8:2A:01:8B:0B:8A:4C:01:F0",
    "fileList": [
      {
        "fileName": "valueMapOthers.txt",
        "codeType": 0,
        "fileType": 3,
        "fileContent": "A23:3.2.5;A24:Android 4.4.2,level 16;A25:hx6DLV78mm9ChnvC;F09:1;C03_testkey:testvalue;C04_APP_ID:a81f9c7e38;"
      }
    ],
    "email": "null",
    "srcIp": "203.205.141.39",
    "uploadTimestamp": 1617970885663,
    "productIdentity": "null",
    "freeSdCard": 0,
    "serverKey": "APP_ID;",
    "isGZIP": 0,
    "cpu": 0,
    "uploadTime": "2021-04-09T12:21:25.663+0000",
    "userKey": "testkey;",
    "romName": "fail%2Ffail",
    "threadName": "null",
    "contactAll": "D8CA9EC44F5556E82A018B0B8A4C01F0",
    "sdkId": "null",
    "callStack": "irgMyesZayrR",
    "fileDir": "null",
    "sdkVersion": "3.2.5",
    "comment": "null",
    "freeStorage": 0
  },
  "launchTime": 9924
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» statusCode|integer|true|none||none|
|» message|string|true|none||none|
|» reqSendTimestamp|integer|true|none||none|
|» rspReceivedTimestamp|integer|true|none||none|
|» rspSendTimestamp|integer|true|none||none|
|» numFound|integer|true|none||none|
|» crashMap|object|true|none||none|
|»» id|string|true|none||none|
|»» issueId|string|true|none||none|
|»» productVersion|string|true|none||none|
|»» model|string|true|none||none|
|»» userId|string|true|none||none|
|»» expMessage|string|true|none||none|
|»» type|string|true|none||none|
|»» processName|string|true|none||none|
|»» retraceStatus|integer|true|none||none|
|»» uploadTime|string|true|none||none|
|»» uploadTimestamp|integer|true|none||none|
|»» crashTime|string|true|none||none|
|»» crashTimestamp|integer|true|none||none|
|»» mergeVersion|string|true|none||none|
|»» messageVersion|string|true|none||none|
|»» isSystemStack|integer|true|none||none|
|»» rqdUuid|string|true|none||none|
|»» retraceResult|string|true|none||none|
|»» appInBack|string|true|none||none|
|»» cpuType|string|true|none||none|
|»» subVersionIssueId|string|true|none||none|
|»» crashId|string|true|none||none|
|»» bundleId|string|true|none||none|
|»» sdkVersion|string|true|none||none|
|»» osVer|string|true|none||none|
|»» expAddr|string|true|none||none|
|»» threadName|string|true|none||none|
|»» memSize|string|true|none||none|
|»» diskSize|string|true|none||none|
|»» imei|string|true|none||none|
|»» imsi|string|true|none||none|
|»» cpuName|string|true|none||none|
|»» brand|string|true|none||none|
|»» freeMem|string|true|none||none|
|»» freeStorage|string|true|none||none|
|»» freeSdCard|string|true|none||none|
|»» mac|string|true|none||none|
|»» country|string|true|none||none|
|»» totalSD|string|true|none||none|
|»» channelId|string|true|none||none|
|»» startTime|string|true|none||none|
|»» startTimestamp|integer|true|none||none|
|»» callStack|string|true|none||none|
|»» retraceCrashDetail|string|true|none||none|
|»» buildNumber|string|true|none||none|
|»» rom|string|true|none||none|
|»» retraceTimestamp|integer|true|none||none|
|»» apn|string|true|none||none|
|»» appInAppstore|boolean|true|none||none|
|»» expName|string|true|none||none|
|»» deviceId|string|true|none||none|
|»» crashCount|integer|true|none||none|
|»» isRooted|string|true|none||none|
|»» isVirtualMachine|integer|true|none||none|
|»» modelOriginalName|string|true|none||none|
|» detailMap|object|true|none||none|
|»» attatchCount|integer|true|none||none|
|»» quaInner|string|true|none||none|
|»» appInfo|string|true|none||none|
|»» stackName|string|true|none||none|
|»» excepitonAddress|string|true|none||none|
|»» retraceCrashDetail|string|true|none||none|
|»» freeMem|integer|true|none||none|
|»» appBaseAddr|string|true|none||none|
|»» battery|integer|true|none||none|
|»» now|string|true|none||none|
|»» archVersion|string|true|none||none|
|»» attachName|string|true|none||none|
|»» tel|string|true|none||none|
|»» id|string|true|none||none|
|»» fileList|[object]|true|none||none|
|»»» fileName|string|false|none||none|
|»»» codeType|integer|false|none||none|
|»»» fileType|integer|false|none||none|
|»»» fileContent|string|false|none||none|
|»» email|string|true|none||none|
|»» srcIp|string|true|none||none|
|»» uploadTimestamp|integer|true|none||none|
|»» productIdentity|string|true|none||none|
|»» freeSdCard|integer|true|none||none|
|»» serverKey|string|true|none||none|
|»» isGZIP|integer|true|none||none|
|»» cpu|integer|true|none||none|
|»» uploadTime|string|true|none||none|
|»» userKey|string|true|none||none|
|»» romName|string|true|none||none|
|»» threadName|string|true|none||none|
|»» contactAll|string|true|none||none|
|»» sdkId|string|true|none||none|
|»» callStack|string|true|none||none|
|»» fileDir|string|true|none||none|
|»» sdkVersion|string|true|none||none|
|»» comment|string|true|none||none|
|»» freeStorage|integer|true|none||none|
|» launchTime|integer|true|none||none|

## GET 获取崩溃详情(支持PC)

GET /env/uniform/openapi/crashDoc

获取崩溃详情(支持PC)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：（移动端）https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_crashDoc.py

（PC端）https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_crashDoc%28pc%29.py

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|appId|query|string| 是 |产品id|
|platformId|query|string| 是 |平台id|
|crashHash|query|string| 是 |崩溃Hash值,crashHash=crashId每2位加：的规则生成|
|fsn|query|string| 否 |fsn值可以写死|
|logtype|query|string| 否 |参数只针对PC有效logtype=interface(自定义日志来自接口)，logtype=file(自定义日志来自文件) logtype=all(自定义日志包括文件和接口)|

> 返回示例

> 200 Response

```json
{
  "statusCode": 0,
  "message": "string",
  "reqSendTimestamp": 0,
  "rspReceivedTimestamp": 0,
  "rspSendTimestamp": 0,
  "numFound": 0,
  "crashMap": {
    "id": "string",
    "issueId": "string",
    "productVersion": "string",
    "model": "string",
    "userId": "string",
    "expMessage": "string",
    "type": "string",
    "processName": "string",
    "retraceStatus": 0,
    "uploadTime": "string",
    "uploadTimestamp": 0,
    "crashTime": "string",
    "crashTimestamp": 0,
    "mergeVersion": "string",
    "messageVersion": "string",
    "isSystemStack": 0,
    "rqdUuid": "string",
    "retraceResult": "string",
    "appInBack": "string",
    "cpuType": "string",
    "subVersionIssueId": "string",
    "crashId": "string",
    "bundleId": "string",
    "sdkVersion": "string",
    "osVer": "string",
    "expAddr": "string",
    "threadName": "string",
    "memSize": "string",
    "diskSize": "string",
    "imei": "string",
    "imsi": "string",
    "cpuName": "string",
    "brand": "string",
    "freeMem": "string",
    "freeStorage": "string",
    "freeSdCard": "string",
    "mac": "string",
    "country": "string",
    "totalSD": "string",
    "channelId": "string",
    "startTime": "string",
    "startTimestamp": 0,
    "callStack": "string",
    "retraceCrashDetail": "string",
    "buildNumber": "string",
    "rom": "string",
    "retraceTimestamp": 0,
    "apn": "string",
    "appInAppstore": true,
    "expName": "string",
    "deviceId": "string",
    "crashCount": 0,
    "isRooted": "string",
    "isVirtualMachine": 0,
    "modelOriginalName": "string"
  },
  "detailMap": {
    "attatchCount": 0,
    "quaInner": "string",
    "appInfo": "string",
    "stackName": "string",
    "excepitonAddress": "string",
    "retraceCrashDetail": "string",
    "freeMem": 0,
    "appBaseAddr": "string",
    "battery": 0,
    "now": "string",
    "archVersion": "string",
    "attachName": "string",
    "tel": "string",
    "id": "string",
    "fileList": [
      {
        "fileName": "string",
        "codeType": 0,
        "fileType": 0,
        "fileContent": "string"
      }
    ],
    "email": "string",
    "srcIp": "string",
    "uploadTimestamp": 0,
    "productIdentity": "string",
    "freeSdCard": 0,
    "serverKey": "string",
    "isGZIP": 0,
    "cpu": 0,
    "uploadTime": "string",
    "userKey": "string",
    "romName": "string",
    "threadName": "string",
    "contactAll": "string",
    "sdkId": "string",
    "callStack": "string",
    "fileDir": "string",
    "sdkVersion": "string",
    "comment": "string",
    "freeStorage": 0
  },
  "launchTime": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» statusCode|integer|true|none||none|
|» message|string|true|none||none|
|» reqSendTimestamp|integer|true|none||none|
|» rspReceivedTimestamp|integer|true|none||none|
|» rspSendTimestamp|integer|true|none||none|
|» numFound|integer|true|none||none|
|» crashMap|object|true|none||none|
|»» id|string|true|none||none|
|»» issueId|string|true|none||none|
|»» productVersion|string|true|none||应用版本|
|»» model|string|true|none||none|
|»» userId|string|true|none||用户id|
|»» expMessage|string|true|none||none|
|»» type|string|true|none||none|
|»» processName|string|true|none||none|
|»» retraceStatus|integer|true|none||还原状态   RESULT_RETRACE_SUCCESS = 0; RESULT_RETRACE_NEED_MAPPINGDATA = 1; RESULT_RETRACE_ERROR = -1; RESULT_RETRACE_NOT_MATCH = -2; RESULT_RETRACE_NO_MAPPING = -3; RESULT_RETRACE_NO_SYSTEM_MATCH = -4; RESULT_RETRACE_NO_SYSTEM_MAPPING = -5; RESULT_RETRACE_CONNECT_ERROR = -6; RESULT_RETRACE_SERVER_BUSY = -7; RESULT_RETRACE_INFO_NOT_ENOUGH = -8; RESULT_RETRACE_NO_SYMBOL = -9; RESULT_RETRACE_MAPPING_DOWNLOADING = -10; RESULT_RETRACE_NO_APPINFO = -11; RESULT_RETRACE_DO_NOTHING = -12;|
|»» uploadTime|string|true|none||上报时间|
|»» uploadTimestamp|integer|true|none||none|
|»» crashTime|string|true|none||发生时间|
|»» crashTimestamp|integer|true|none||none|
|»» mergeVersion|string|true|none||none|
|»» messageVersion|string|true|none||none|
|»» isSystemStack|integer|true|none||none|
|»» rqdUuid|string|true|none||none|
|»» retraceResult|string|true|none||none|
|»» appInBack|string|true|none||none|
|»» cpuType|string|true|none||cpu架构|
|»» subVersionIssueId|string|true|none||none|
|»» crashId|string|true|none||none|
|»» bundleId|string|true|none||应用包名|
|»» sdkVersion|string|true|none||none|
|»» osVer|string|true|none||系统版本|
|»» expAddr|string|true|none||异常进程#线程|
|»» threadName|string|true|none||none|
|»» memSize|string|true|none||none|
|»» diskSize|string|true|none||none|
|»» imei|string|true|none||none|
|»» imsi|string|true|none||none|
|»» cpuName|string|true|none||none|
|»» brand|string|true|none||none|
|»» freeMem|string|true|none||none|
|»» freeStorage|string|true|none||none|
|»» freeSdCard|string|true|none||none|
|»» mac|string|true|none||none|
|»» country|string|true|none||none|
|»» totalSD|string|true|none||none|
|»» channelId|string|true|none||none|
|»» startTime|string|true|none||none|
|»» startTimestamp|integer|true|none||none|
|»» callStack|string|true|none||还原前堆栈信息|
|»» retraceCrashDetail|string|true|none||还原后堆栈信息|
|»» buildNumber|string|true|none||none|
|»» rom|string|true|none||none|
|»» retraceTimestamp|integer|true|none||none|
|»» apn|string|true|none||none|
|»» appInAppstore|boolean|true|none||none|
|»» expName|string|true|none||none|
|»» deviceId|string|true|none||设备id|
|»» crashCount|integer|true|none||none|
|»» isRooted|string|true|none||none|
|»» isVirtualMachine|integer|true|none||是否是模拟器|
|»» modelOriginalName|string|true|none||设备机型|
|» detailMap|object|true|none||none|
|»» attatchCount|integer|true|none||none|
|»» quaInner|string|true|none||none|
|»» appInfo|string|true|none||none|
|»» stackName|string|true|none||none|
|»» excepitonAddress|string|true|none||none|
|»» retraceCrashDetail|string|true|none||none|
|»» freeMem|integer|true|none||none|
|»» appBaseAddr|string|true|none||none|
|»» battery|integer|true|none||none|
|»» now|string|true|none||none|
|»» archVersion|string|true|none||none|
|»» attachName|string|true|none||none|
|»» tel|string|true|none||none|
|»» id|string|true|none||none|
|»» fileList|[object]|true|none||none|
|»»» fileName|string|false|none||none|
|»»» codeType|integer|false|none||none|
|»»» fileType|integer|false|none||none|
|»»» fileContent|string|false|none||none|
|»» email|string|true|none||none|
|»» srcIp|string|true|none||none|
|»» uploadTimestamp|integer|true|none||none|
|»» productIdentity|string|true|none||none|
|»» freeSdCard|integer|true|none||none|
|»» serverKey|string|true|none||none|
|»» isGZIP|integer|true|none||none|
|»» cpu|integer|true|none||none|
|»» uploadTime|string|true|none||none|
|»» userKey|string|true|none||none|
|»» romName|string|true|none||none|
|»» threadName|string|true|none||none|
|»» contactAll|string|true|none||none|
|»» sdkId|string|true|none||none|
|»» callStack|string|true|none||none|
|»» fileDir|string|true|none||none|
|»» sdkVersion|string|true|none||none|
|»» comment|string|true|none||none|
|»» freeStorage|integer|true|none||none|
|» launchTime|integer|true|none||none|

## POST 获取趋势数据(今天-累计)(新鉴权)

POST /env/uniform/openapi/getAppRealTimeTrendAppendEx

获取趋势数据(今天-累计)(新鉴权)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例： https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getAppRealTimeTrendAppendEx.py

> Body 请求参数

```json
"{\r\n    \"appId\": \"9f2dcbd9ab\",\r\n    \"platformId\": 1,\r\n    \"startDate\": \"2023062800\",\r\n    \"endDate\": \"2023062800\",\r\n    \"type\": \"crash\",\r\n    \"fsn\": \"\",\r\n    \"dataType\": \"\",\r\n    \"vm\": 0,\r\n    \"versionList\": \"[\\\"8.4.1.1.804010199\\\",\\\"3.82.1.4\\\"]\",\r\n    \"needCountryDimension\": false,\r\n    \"countryList\": \"\",\r\n    \"mergeMultipleVersionsWithInaccurateResult\": True\r\n}"
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Content-Type|header|string| 否 |none|
|Accept-Encoding|header|string| 否 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |产品id|
|» platformId|body|integer| 是 |平台id|
|» startDate|body|string| 是 |开始时间 YYMMDDHH|
|» endDate|body|string| 是 |结束时间 YYMMDDHH|
|» type|body|string| 是 |三种类型-crash,anr,error|
|» fsn|body|string| 是 |fsn值可以写死|
|» dataType|body|string| 是 |realTimeTrendData|
|» vm|body|integer| 是 |0 全量 1 真机 2 模拟器|
|» versionList|body|string| 是 |如果需要查询多版本，使用versionList。这时候不需要填写version字段。版本支持通配符*。|
|» needCountryDimension|body|boolean| 否 |true: 需要国家维度的统计 false: 不需要|
|» countryList|body|string| 否 |如果设置了需要国家维度的统计，则传入需要查询的国家名称列表。如果设置了needCountryDimension但countryList为空数组，则表示查询全部国家地区|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| 否 |多版本的结果是否要合并。|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "",
    "data": [
      {
        "appId": "9f2dcbd9ab",
        "platformId": 1,
        "version": "NO_STATS_DATA",
        "date": "2023062800",
        "crashNum": 0,
        "crashUser": 0,
        "reportNumAllData": 0,
        "reportDeviceAllData": 0,
        "accessNum": 0,
        "accessUser": 0,
        "country": "NO_STATS_DATA"
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» reportNumAllData|integer|true|none||none|
|» reportDeviceAllData|integer|true|none||none|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|
|» country|string|true|none||none|

## POST 获取跟踪数据，跟踪日志，其他信息，自定义kv等

POST /env/uniform/openapi/appDetailCrash

> Body 请求参数

```json
{
  "appId": "string",
  "platformId": "string",
  "crashHash": "string",
  "fsn": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» appId|body|string| 是 | 产品id|none|
|» platformId|body|string| 是 | 平台id|none|
|» crashHash|body|string| 是 ||none|
|» fsn|body|string| 否 ||none|

> 返回示例

```json
{
  "attachList": [
    {
      "fileName": "valueMapOthers.txt",
      "fileType": 3,
      "content": "A23:3.2.5;A24:Android 4.4.2,level 16;A25:hx6DLV78mm9ChnvC;F09:1;C03_testkey:testvalue;C04_APP_ID:a81f9c7e38;"
    }
  ],
  "sysLogs": [
    "Report: stack frame :2, has cause false",
    "05-07 17:20:13.626  4883  5108 I CrashReport: try to upload right now",
    "05-07 17:20:13.626  4883  5108 D CrashReport: Uploading frequency will not be checked if SDK is in debug mode.",
    "05-07 17:20:13.626  4883  5108 D CrashReport: java.lang.RuntimeException rid:af4470df-c99f-4553-8c64-7c4cc44ecc44 sess:1264696e-5c31-4370-a7ac-f80e08352557 ls:5328s isR:false isF:true isM:false isN:false mc:0 ,null ,isUp:false ,vm:33",
    "05-07 17:20:13.646  4883  5108 D dalvikvm: GC_FOR_ALLOC freed 494K, 54% free 4512K/9704K, paused 4ms, total 4ms",
    "05-07 17:20:13.646  4883  5108 D CrashReport: [UploadManager] Add upload task (pid=4883 | tid=5108)",
    "05-07 17:20:13.646  4883  5108 D CrashReport: [UploadManager] Sucessfully got session ID, try to execute upload task now (pid=4883 | tid=5108)"
  ],
  "userLogs": [
    ""
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» attachList|[object]|true|none||none|
|»» fileName|string|false|none||none|
|»» fileType|integer|false|none||none|
|»» content|string|false|none||none|
|» sysLogs|[string]|true|none||none|
|» userLogs|[string]|true|none||none|

## GET 获取跟踪数据，跟踪日志，其他信息，自定义kv等

GET /env/uniform/openapi/appDetailCrash

获取跟踪数据，跟踪日志，其他信息，自定义kv等

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|appId|query|string| 是 ||产品id|
|platformId|query|string| 是 ||平台id|
|crashHash|query|string| 是 ||none|
|fsn|query|string| 是 ||	|

#### 详细说明

**fsn**: 	
fsn值可以写死

> 返回示例

> 200 Response

```json
{
  "attachList": [
    {
      "fileName": "string",
      "fileType": 0,
      "content": "string"
    }
  ],
  "sysLogs": [
    "string"
  ],
  "userLogs": [
    "string"
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» attachList|[object]|true|none||none|
|»» fileName|string|false|none||文件名字|
|»» fileType|integer|false|none||文件类型|
|»» content|string|false|none||文件内容，自定义kv|
|» sysLogs|[string]|true|none||其他信息|
|» userLogs|[string]|true|none||跟踪日志|

## POST 根据issue获取crashHash列表 (支持PC)

POST /env/uniform/openapi/crashList

> Body 请求参数

```json
{
  "appId": "7786d1a114",
  "crashDataType": "undefined",
  "start": 0,
  "searchType": "detail",
  "exceptionTypeList": "",
  "pid": 1,
  "platformId": 1,
  "issueId": "F3B213561B26E0C45A6C397CD77668D9",
  "rows": 10,
  "version": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||none|
|» crashDataType|body|string| 是 ||none|
|» start|body|integer| 是 ||none|
|» searchType|body|string| 是 ||none|
|» exceptionTypeList|body|string| 是 ||none|
|» pid|body|integer| 是 ||none|
|» platformId|body|integer| 是 ||none|
|» issueId|body|string| 是 ||none|
|» rows|body|integer| 是 ||none|
|» version|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "statusCode": 0,
  "message": null,
  "reqSendstamp": 0,
  "rspReceivedTiamp": 0,
  "rspSendTimestamp": 0,
  "numFound": 0,
  "issueList": [
    "string"
  ],
  "crashIdList": [
    "string"
  ],
  "crashDatas": {
    "337A2BABD0DBA145C462625FD26BD349": {
      "productVersion": "string",
      "dumpId": "string",
      "model": "string",
      "id": "string",
      "uploadTime": "string",
      "crashId": "string",
      "osVer": "string",
      "deviceId": "string",
      "userId": "string"
    }
  },
  "detailDatas": null,
  "tagInfoList": null,
  "tagList": null,
  "crashNums": 0,
  "anrNums": 0,
  "errorNums": 0,
  "scrollId": null
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» statusCode|integer|true|none||none|
|» message|null|true|none||none|
|» reqSendstamp|integer|true|none||none|
|» rspReceivedTiamp|integer|true|none||none|
|» rspSendTimestamp|integer|true|none||none|
|» numFound|integer|true|none||none|
|» issueList|[string]|true|none||none|
|» crashIdList|[string]|true|none||none|
|» crashDatas|object|true|none||崩溃详情  crashDatas包含dumpid(dump文件域名 + dumpid + ".dmp.gz ")|
|»» 337A2BABD0DBA145C462625FD26BD349|object|true|none||none|
|»»» productVersion|string|true|none||none|
|»»» dumpId|string|true|none||none|
|»»» model|string|true|none||none|
|»»» id|string|true|none||none|
|»»» uploadTime|string|true|none||none|
|»»» crashId|string|true|none||none|
|»»» osVer|string|true|none||none|
|»»» deviceId|string|true|none||none|
|»»» userId|string|true|none||none|
|» detailDatas|null|true|none||none|
|» tagInfoList|null|true|none||none|
|» tagList|null|true|none||none|
|» crashNums|integer|true|none||none|
|» anrNums|integer|true|none||none|
|» errorNums|integer|true|none||none|
|» scrollId|null|true|none||none|

## GET 根据issue获取crashHash列表 (支持PC)

GET /env/uniform/openapi/crashList

根据issue获取crashHash列表(支持PC)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：（移动端）https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/openapi/crashsight_openapi_v1_crashList.py

（PC端）https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/openapi/crashsight_openapi_v1_crashList(pc).py

> Body 请求参数

```json
{
  "appId": "7786d1a114",
  "crashDataType": "undefined",
  "start": 0,
  "searchType": "detail",
  "exceptionTypeList": "",
  "pid": 1,
  "platformId": 1,
  "issueId": "F3B213561B26E0C45A6C397CD77668D9",
  "rows": 10,
  "version": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品id|
|» crashDataType|body|string| 是 ||默认undefined|
|» start|body|integer| 是 ||从第几页开始，默认0|
|» searchType|body|string| 是 ||默认detail|
|» exceptionTypeList|body|string| 是 ||类型 崩溃分析（Crash%2CNative%2CExtensionCrash） ANR分析(ANR) 错误分析(AllCatched%2CUnity3D%2CLua%2CJS)|
|» pid|body|integer| 是 ||默认 10|
|» platformId|body|integer| 是 ||平台id,1是安卓,2是ios，10是PC|
|» issueId|body|string| 是 ||问题id|
|» rows|body|integer| 是 ||每一页条数|
|» version|body|string| 是 ||否	可选，需要过滤的版本号|

> 返回示例

> 200 Response

```json
{
  "statusCode": 0,
  "message": null,
  "reqSendstamp": 0,
  "rspReceivedTiamp": 0,
  "rspSendTimestamp": 0,
  "numFound": 0,
  "issueList": [
    "string"
  ],
  "crashIdList": [
    "string"
  ],
  "crashDatas": {
    "337A2BABD0DBA145C462625FD26BD349": {
      "productVersion": "string",
      "dumpId": "string",
      "model": "string",
      "id": "string",
      "uploadTime": "string",
      "crashId": "string",
      "osVer": "string",
      "deviceId": "string",
      "userId": "string"
    }
  },
  "detailDatas": null,
  "tagInfoList": null,
  "tagList": null,
  "crashNums": 0,
  "anrNums": 0,
  "errorNums": 0,
  "scrollId": null
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» statusCode|integer|true|none||none|
|» message|null|true|none||none|
|» reqSendstamp|integer|true|none||none|
|» rspReceivedTiamp|integer|true|none||none|
|» rspSendTimestamp|integer|true|none||none|
|» numFound|integer|true|none||none|
|» issueList|[string]|true|none||none|
|» crashIdList|[string]|true|none||none|
|» crashDatas|object|true|none||崩溃详情  crashDatas包含dumpid(dump文件域名 + dumpid + ".dmp.gz ")|
|»» 337A2BABD0DBA145C462625FD26BD349|object|true|none||none|
|»»» productVersion|string|true|none||none|
|»»» dumpId|string|true|none||none|
|»»» model|string|true|none||none|
|»»» id|string|true|none||none|
|»»» uploadTime|string|true|none||none|
|»»» crashId|string|true|none||none|
|»»» osVer|string|true|none||none|
|»»» deviceId|string|true|none||none|
|»»» userId|string|true|none||none|
|» detailDatas|null|true|none||none|
|» tagInfoList|null|true|none||none|
|» tagList|null|true|none||none|
|» crashNums|integer|true|none||none|
|» anrNums|integer|true|none||none|
|» errorNums|integer|true|none||none|
|» scrollId|null|true|none||none|

## POST 获取趋势数据(小时粒度)(新鉴权)

POST /env/uniform/openapi/getRealTimeHourlyStatEx

获取趋势数据(今天-按小时)(新鉴权)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getRealTimeHourlyStatEx.py

> Body 请求参数

```json
"{\r\n    \"appId\": \"f4f1ae20c0\",\r\n    \"platformId\": 1,\r\n    \"version\": \"\",\r\n    \"versionList\": \"[\\\"8.4.1.1.804010199\\\",\\\"3.82.1.4\\\"]\",\r\n    \"startDate\": \"2023070500\",\r\n    \"endDate\": \"2023070523\",\r\n    \"type\": \"\",\r\n    \"fsn\": \"\",\r\n    \"dataType\": \"realTimeTrendData\",\r\n    \"vm\": 0,\r\n    \"needCountryDimension\": False,\r\n    \"countryList\": \"[]\",\r\n    \"mergeMultipleVersionsWithInaccurateResult\": True\r\n}"
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品id|
|» platformId|body|integer| 是 ||平台类型，安卓端：1，iOS端：2，PC端：10|
|» version|body|string| 是 ||默认全版本，-1|
|» versionList|body|string| 是 ||如果需要查询多版本，使用versionList。这时候不需要填写version字段。版本支持通配符*。|
|» startDate|body|string| 是 ||开始时间 YYMMDDHH|
|» endDate|body|string| 是 ||结束时间 YYMMDDHH|
|» type|body|string| 是 ||异常类型，crash，anr，error|
|» fsn|body|string| 是 ||fsn值可以写死|
|» dataType|body|string| 是 ||realTimeTrendData|
|» vm|body|integer| 是 ||0全量1真机2模拟器|
|» needCountryDimension|body|boolean| 否 ||true: 需要国家维度的统计 false: 不需要|
|» countryList|body|string| 否 ||如果设置了需要国家维度的统计，则传入需要查询的国家名称列表。如果设置了needCountryDimension但countryList为空数组，则表示查询全部国家地区|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| 否 ||多版本的结果是否要合并。|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "",
    "data": [
      {
        "appId": "f4f1ae20c0",
        "platformId": 1,
        "version": "MERGED",
        "date": "2023070500",
        "crashNum": 1,
        "crashUser": 1,
        "reportNumAllData": 0,
        "reportDeviceAllData": 0,
        "accessNum": 53,
        "accessUser": 19,
        "country": "-1"
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||产品id|
|» platformId|integer|true|none||平台id|
|» version|string|true|none||项目版本|
|» date|string|true|none||时间|
|» crashNum|integer|true|none||崩溃次数|
|» crashUser|integer|true|none||崩溃用户数|
|» reportNumAllData|integer|true|none||none|
|» reportDeviceAllData|integer|true|none||none|
|» accessNum|integer|true|none||联网次数|
|» accessUser|integer|true|none||联网用户数|
|» country|string|true|none||none|

## POST 设置问题级标签(新鉴权)

POST /env/uniform/openapi/addTag

设置问题级标签(新鉴权)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

> Body 请求参数

```json
{
  "appId": "3729de3c06",
  "platformId": 1,
  "issueId": "3A88972A6C00AF25C9038A870B40867D",
  "tagName": "1111"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品ID|
|» platformId|body|integer| 是 ||平台ID|
|» issueId|body|string| 是 ||问题ID|
|» tagName|body|string| 是 ||问题标签|

> 返回示例

> 200 Response

```json
{
  "status": 0,
  "ret": {
    "statusCode": 0,
    "message": "string",
    "tagInfoList": {
      "tagId": 0,
      "tagName": "string"
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||响应状态|
|» ret|object|true|none||查询结果|
|»» statusCode|integer|true|none||查询状态码|
|»» message|string|true|none||错误详情|
|»» tagInfoList|object|true|none||标签列表|
|»»» tagId|integer|true|none||系统标签Id|
|»»» tagName|string|true|none||标签名|

## POST 崩溃分析高级搜索(新鉴权)

POST /uniform/openapi/advancedSearch

崩溃分析

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

> Body 请求参数

```json
{
  "searchType": "detail",
  "exceptionTypeList": "Crash",
  "sortOrder": "desc",
  "sortField": "imeiCount",
  "appId": "5df4e62f02",
  "platformId": 1,
  "rows": 10,
  "fsn": "",
  "date": "last_7_day",
  "startDateStr": "",
  "endDateStr": "",
  "crashTimeBeginMillis": "1683796369056",
  "crashTimeEndMillis": "1683969175056",
  "status": "0",
  "version": "",
  "deviceIdList": "491b9e04-7f8f-428c-8cb7-00fddbb1bd27",
  "bundleId": "com.lilithgame.wgame.android.cn"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» searchType|body|string| 是 ||查询类型|
|» exceptionTypeList|body|string| 是 ||异常类型list|
|» sortOrder|body|string| 是 ||排序类型|
|» sortField|body|string| 是 ||排序字段|
|» appId|body|string| 是 ||项目id|
|» platformId|body|integer| 是 ||平台id|
|» rows|body|integer| 是 ||获取行数|
|» fsn|body|string| 是 ||可以写死|
|» date|body|string| 是 ||按照时间段搜索 不传这个字段就是所有时间 last_1_hour(最近1小时) last_2_day(最近2天) last_7_day(最近7天) last_15_day(最近15天) last_30_day(最近30天) custom|
|» startDateStr|body|string| 否 ||起始时间 （格式：2023-05-02,仅date：custom才生效）|
|» endDateStr|body|string| 否 ||结束时间 （格式：2023-05-02,仅date：custom才生效）|
|» crashTimeBeginMillis|body|string| 否 ||发生时间（精确到毫秒,"1683820801101"）闪退时间字段|
|» crashTimeEndMillis|body|string| 否 ||结束时间（精确到毫秒,"1683820801101"）闪退时间字段|
|» status|body|string| 否 ||可选，按照问题处理状态过滤 0：未处理 1： 已处理 2： 处理中 支持多选，用英文逗号连接，例如 0,2 表示过滤未处理或处理中|
|» version|body|string| 是 ||版本支持通配符*，前缀匹配。|
|» deviceIdList|body|string| 是 ||设备的uuid(唯一序列号)|
|» bundleId|body|string| 是 ||闪退应用得包名|

> 返回示例

```json
{
  "status": 200,
  "ret": 200,
  "data": {
    "statusCode": 0,
    " appId": "",
    "platformId": "",
    "message": "null",
    "reqSendTimestamp": 0,
    "rspReceivedTimestamp": 0,
    "rspSendTimestamp": 0,
    "numFound": 3,
    "queryInaccurateReason": "null",
    "issueList": {
      "issueId": "3A88972A6C00AF25C9038A870B40867D",
      "exceptionName": "ANR_EXCEPTION",
      "exceptionMessage": "ANR Input dispatching timed out (Waiting because the touched window has not finished processing the input events that were previously delivered to it.)",
      "keyStack": "com.tencent.bugly.demo.MainActivity$45.onClick(MainActivity.java:1045)",
      "lastestUploadTime": "2023-05-12 18:11:04 378",
      "latestUploadTimestamp": 1663594030011,
      "imeiCount": 1125058,
      "sysImeiCount": 0,
      "count": 1125116,
      "sysCount": 0,
      "version": "#$cv#$",
      "tagInfoList": [],
      "processor": "",
      "status": 0,
      "firstUploadTime": "2022-09-19 21:27:10 011",
      "firstUploadTimestamp": 1663594030011,
      "firstCrashVersion": "1.0.3",
      "issueHash": "3A:88:97:2A:6C:00:AF:25:C9:03:8A:87:0B:40:86:7D",
      "ftName": "",
      "issueVersions": [
        {
          "version": "1.0.3",
          "firstUploadTime": "null",
          "firstUploadTimestamp": 0,
          "lastUploadTime": "null",
          "lastUploadTimestamp": 0,
          "count": 0,
          "deviceCount": 0,
          "systemExitCount": 0,
          "systemExitDeviceCount": 0
        }
      ],
      "detailId": "",
      "parentHash": "",
      "bugs": null,
      "crossVerStat": 2,
      "issueExceptionType": 3,
      "issueCount": 1,
      "deviceMatchCount": null,
      "tagList": [],
      "tag": null,
      "esMap": {
        "issueId": "3A88972A6C00AF25C9038A870B40867D",
        "firstCrashVersion": "1.0.3",
        "mergeType": 0,
        "count": 1125116,
        "stackLineStatus": 0,
        "issueExceptionType": 3,
        "firstTime": "2022-09-19 21:27:10 011",
        "firstTimestamp": 1663594030011,
        "systemImeiCount": 0,
        "crossVerStat": 2,
        "systemCount": 0,
        "expireTime": 1667050030108,
        "issueUploadTimestamp": 1663594030011,
        "issueHash": "3A88972A6C00AF25C9038A870B40867D",
        "keyStack": "com.tencent.bugly.demo.MainActivity$45.onClick(MainActivity.java:1045)",
        "issueUploadTime": "2023-05-12 18:11:04 378",
        "issueAppId": "3729de3c06",
        "stackType": 2,
        "hotVer": "",
        "issueVersion": "#$cv#$",
        "exceptionMessage": "ANR Input dispatching timed out (Waiting because the touched window has not finished processing the input events that were previously delivered to it.)",
        "issueErrorType": "ANR_EXCEPTION",
        "imeiCount": 1125058,
        "status": 0
      },
      "esCount": 1125116,
      "esDeviceCount": 1125058
    },
    "crashIdList": [],
    "crashDatas": {},
    "detailDatas": null,
    "tagInfoList": null,
    "tagList": null,
    "crashNums": 1,
    "anrNums": 1,
    "errorNums": 1,
    "totalCrashMatchCount": 3,
    "scrollId": null
  },
  "message": "OK",
  "errorCode": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||响应状态|
|» ret|integer|true|none||none|
|» data|object|true|none||查询结果|
|»» statusCode|integer|true|none||none|
|»»  appId|string|true|none||项目id|
|»» platformId|string|true|none||平台id|
|»» message|string|true|none||none|
|»» reqSendTimestamp|integer|true|none||none|
|»» rspReceivedTimestamp|integer|true|none||none|
|»» rspSendTimestamp|integer|true|none||none|
|»» numFound|integer|true|none||异常总数|
|»» queryInaccurateReason|string|true|none||none|
|»» issueList|object|true|none||issuse列表|
|»»» issueId|string|true|none||none|
|»»» exceptionName|string|true|none||异常名字|
|»»» exceptionMessage|string|true|none||异常消息|
|»»» keyStack|string|true|none||堆栈信息|
|»»» lastestUploadTime|string|true|none||最近一次上报时间|
|»»» latestUploadTimestamp|integer|true|none||none|
|»»» imeiCount|integer|true|none||none|
|»»» sysImeiCount|integer|true|none||none|
|»»» count|integer|true|none||发生次数|
|»»» sysCount|integer|true|none||none|
|»»» version|string|true|none||none|
|»»» tagInfoList|[string]|true|none||标签信息列表|
|»»» processor|string|true|none||issue处理人|
|»»» status|integer|true|none||issue状态|
|»»» firstUploadTime|string|true|none||none|
|»»» firstUploadTimestamp|integer|true|none||none|
|»»» firstCrashVersion|string|true|none||none|
|»»» issueHash|string|true|none||none|
|»»» ftName|string|true|none||none|
|»»» issueVersions|[object]|true|none||子issue版本|
|»»»» version|string|false|none||none|
|»»»» firstUploadTime|string|false|none||none|
|»»»» firstUploadTimestamp|integer|false|none||none|
|»»»» lastUploadTime|string|false|none||none|
|»»»» lastUploadTimestamp|integer|false|none||none|
|»»»» count|integer|false|none||none|
|»»»» deviceCount|integer|false|none||none|
|»»»» systemExitCount|integer|false|none||none|
|»»»» systemExitDeviceCount|integer|false|none||none|
|»»» detailId|string|true|none||none|
|»»» parentHash|string|true|none||none|
|»»» bugs|null|true|none||none|
|»»» crossVerStat|integer|true|none||none|
|»»» issueExceptionType|integer|true|none||none|
|»»» issueCount|integer|true|none||none|
|»»» deviceMatchCount|null|true|none||none|
|»»» tagList|[string]|true|none||none|
|»»» tag|null|true|none||none|
|»»» esMap|object|true|none||none|
|»»»» issueId|string|true|none||none|
|»»»» firstCrashVersion|string|true|none||none|
|»»»» mergeType|integer|true|none||none|
|»»»» count|integer|true|none||none|
|»»»» stackLineStatus|integer|true|none||none|
|»»»» issueExceptionType|integer|true|none||none|
|»»»» firstTime|string|true|none||none|
|»»»» firstTimestamp|integer|true|none||none|
|»»»» systemImeiCount|integer|true|none||none|
|»»»» crossVerStat|integer|true|none||none|
|»»»» systemCount|integer|true|none||none|
|»»»» expireTime|integer|true|none||none|
|»»»» issueUploadTimestamp|integer|true|none||none|
|»»»» issueHash|string|true|none||none|
|»»»» keyStack|string|true|none||none|
|»»»» issueUploadTime|string|true|none||none|
|»»»» issueAppId|string|true|none||none|
|»»»» stackType|integer|true|none||none|
|»»»» hotVer|string|true|none||none|
|»»»» issueVersion|string|true|none||none|
|»»»» exceptionMessage|string|true|none||none|
|»»»» issueErrorType|string|true|none||none|
|»»»» imeiCount|integer|true|none||none|
|»»»» status|integer|true|none||none|
|»»» esCount|integer|true|none||none|
|»»» esDeviceCount|integer|true|none||none|
|»» crashIdList|[string]|true|none||none|
|»» crashDatas|object|true|none||none|
|»» detailDatas|null|true|none||none|
|»» tagInfoList|null|true|none||none|
|»» tagList|null|true|none||none|
|»» crashNums|integer|true|none||崩溃总数|
|»» anrNums|integer|true|none||ANR总数|
|»» errorNums|integer|true|none||错误总数|
|»» totalCrashMatchCount|integer|true|none||none|
|»» scrollId|null|true|none||none|
|» message|string|true|none||none|
|» errorCode|string|true|none||none|

## POST 用户最近3日异常数据上报

POST /env/uniform/openapi/queryAccessList

用户最近3日异常数据上报

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_queryAccessList.py

> Body 请求参数

```json
{
  "uploadTimeBeginMillis": 1701757736151,
  "deviceIdList": [
    "PyQ4c3MD55tgowUv"
  ],
  "userIdList": [
    "YQWUOpt"
  ],
  "appId": "3729de3c06",
  "platformId": 1,
  "skipDistinctQuery": true,
  "pageNumber": 1,
  "pageSize": 3000
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» uploadTimeBeginMillis|body|integer| 是 ||起始时间(只保存了近三天数据) 单位：ms|
|» deviceIdList|body|[string]| 是 ||设备Id列表 可选字段与userIdList二选一|
|» userIdList|body|[string]| 是 ||用户Id列表 可选字段与deviceIdList二选一|
|» appId|body|string| 是 ||项目ID|
|» platformId|body|integer| 是 ||平台ID|
|» skipDistinctQuery|body|boolean| 是 ||none|
|» pageNumber|body|integer| 是 ||none|
|» pageSize|body|integer| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "status": 0,
  "ret": 0,
  "data": {
    "result": {
      "records": [
        {
          "appId": "string",
          "platformId": 0,
          "uploadTime": "string",
          "userId": "string",
          "deviceId": "string",
          "issueId": "string",
          "crashId": "string",
          "launchTimeMillisStr": "string",
          "expMessage": "string",
          "productVersion": "string",
          "csType": "string",
          "model": "string",
          "networkType": "string",
          "clientIp": "string",
          "uploadIp": "string",
          "isCoolStart": true
        }
      ],
      "total": 0,
      "size": 0,
      "current": 0,
      "orders": [
        "string"
      ],
      "optimizeCountSql": true,
      "searchCount": true,
      "pages": 0
    }
  },
  "message": "string",
  "errorCode": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|integer|true|none||none|
|» data|object|true|none||none|
|»» result|object|true|none||none|
|»»» records|[object]|true|none||上传记录|
|»»»» appId|string|false|none||项目ID|
|»»»» platformId|integer|false|none||平台ID|
|»»»» uploadTime|string|false|none||上传时间|
|»»»» userId|string|false|none||用户ID|
|»»»» deviceId|string|false|none||设备ID|
|»»»» issueId|string|false|none||问题ID|
|»»»» crashId|string|false|none||异常ID|
|»»»» launchTimeMillisStr|string|false|none||启动时间|
|»»»» expMessage|string|false|none||异常信息|
|»»»» productVersion|string|false|none||应用版本|
|»»»» csType|string|false|none||消息类型|
|»»»» model|string|false|none||机型|
|»»»» networkType|string|false|none||none|
|»»»» clientIp|string|false|none||none|
|»»»» uploadIp|string|false|none||none|
|»»»» isCoolStart|boolean|false|none||none|
|»»» total|integer|true|none||none|
|»»» size|integer|true|none||none|
|»»» current|integer|true|none||none|
|»»» orders|[string]|true|none||none|
|»»» optimizeCountSql|boolean|true|none||none|
|»»» searchCount|boolean|true|none||none|
|»»» pages|integer|true|none||none|
|» message|string|true|none||none|
|» errorCode|string|true|none||none|

## POST 根据堆栈关键字获取机型列表(国内)

POST /env/uniform/openapi/getStackDeviceInfo

> Body 请求参数

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "stime": "2023-02-28 00:00:00",
  "etime": "2023-03-01 00:00:00",
  "source": 0,
  "params": {
    "keyName": "*"
  },
  "limit": 0,
  "type": "pretty"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 是 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» source|body|integer| 否 ||环境参数|
|» params|body|object| 否 ||筛选条件|
|»» keyName|body|string| 否 ||堆栈关键字（支持*通配符）|
|» limit|body|integer| 否 ||返回条数|
|» type|body|string| 否 ||返回格式 Json "type":"pretty" 默认返回值域和列值|

> 返回示例

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "keyName": "*",
        "model": "魅族 M6",
        "osVersion": "Android 4.4.2,level 20",
        "crashNums": 4800,
        "crashUsers": 4800
      }
    ]
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|false|none||请求id|
|» code|integer|false|none||状态码|
|» errmsg|string|false|none||错误详情|
|» data|object|false|none||查询数据|
|»» columns|null|true|none||键值|
|»» values|null|true|none||值域|
|»» results|[object]|true|none||查询详情|
|»»» keyName|string|false|none||none|
|»»» model|string|false|none||none|
|»»» osVersion|string|false|none||none|
|»»» crashNums|integer|false|none||none|
|»»» crashUsers|integer|false|none||none|
|» cost|integer|false|none||查询耗时|

## POST 获取时间段内崩溃用户列表

POST /env/uniform/openapi/getCrashUserList

获取时间段内崩溃用户列表

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/openapi/crashsight_openapi_v1_getCrashUserList.py

> Body 请求参数

```json
{
  "requestid": "",
  "stime": "2022-10-19 00:00:00",
  "etime": "2022-10-20 00:00:00",
  "source": 0,
  "limit": 0,
  "type": "",
  "appId": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 否 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» source|body|integer| 否 ||环境参数|
|» limit|body|integer| 否 ||返回条数|
|» type|body|string| 否 ||返回格式|
|» appId|body|string| 是 ||项目appid|

> 返回示例

```json
{
  "requestid": "null",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": [
      "user"
    ],
    "values": [
      [
        "1178710688500659"
      ]
    ],
    "results": null
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||none|
|» code|integer|true|none||none|
|» errmsg|string|true|none||none|
|» data|object|true|none||none|
|»» columns|[string]|true|none||none|
|»» values|[array]|true|none||none|
|»» results|null|true|none||none|
|» cost|integer|true|none||none|

## POST 根据堆栈关键字获取崩溃统计

POST /env/uniform/openapi/getStackCrashStat

根据堆栈关键字获取崩溃统计

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例： https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/openapi/crashsight_openapi_v1_getStackCrashStat.py

> Body 请求参数

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "stime": "2022-10-15 00:00:00",
  "etime": "2022-10-16 00:00:00",
  "source": 0,
  "params": {
    "keyName": "*"
  },
  "limit": 0,
  "type": "pretty",
  "appId": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 否 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» source|body|integer| 否 ||环境参数|
|» params|body|object| 否 ||筛选条件|
|»» keyName|body|string| 否 ||堆栈关键字（支持*通配符）|
|» limit|body|integer| 否 ||返回条数|
|» type|body|string| 否 ||返回格式 Json "type":"pretty" 默认返回值域和列值|
|» appId|body|string| 是 ||产品id|

> 返回示例

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "keyName": "*",
        "crashNums": 4799,
        "crashUsers": 4799
      }
    ]
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||请求id|
|» code|integer|true|none||状态码|
|» errmsg|string|true|none||错误详情|
|» data|object|true|none||查询数据|
|»» columns|null|true|none||键值|
|»» values|null|true|none||值域|
|»» results|[object]|true|none||查询详情|
|»»» keyName|string|false|none||none|
|»»» crashNums|integer|false|none||none|
|»»» crashUsers|integer|false|none||none|
|» cost|integer|true|none||查询耗时|

## POST 根据deviceId获取崩溃列表

POST /env/uniform/openapi/getCrashDeviceStat

/uniform/openapi/getCrashDeviceStat/platformId/1  安卓
/uniform/openapi/getCrashDeviceStat/platformId/2  IOS
/uniform/openapi/getCrashDeviceStat/platformId/10  PC

> Body 请求参数

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "stime": "2022-08-30 00:00:00",
  "etime": "2022-08-31 00:00:00",
  "filters": {
    "deviceId": "[\"37138989-52b1-4bcb-8bc2-b750270a1e6c\"]"
  },
  "limit": 0,
  "type": "pretty"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 是 ||application/json|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» filters|body|object| 否 ||筛选条件|
|»» deviceId|body|string| 否 ||deviceId列表|
|» limit|body|integer| 否 ||返回条数|
|» type|body|string| 否 ||返回格式 17.Json "type":"pretty" 18.默认返回值域和列值|

> 返回示例

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "exceptionType": "java.lang.NullPointerException",
        "deviceId": "37138989-52b1-4bcb-8bc2-b750270a1e6c",
        "issueId": "040920EBBAAAA011B35C8D38429BF4BC",
        "crashId": "F8E9EFC12593701F6F0BDCDB500D8965",
        "user": "979878",
        "hardware": "M2012K10C",
        "model": "M2012K10C"
      }
    ]
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||请求id|
|» code|integer|true|none||状态码|
|» errmsg|string|true|none||错误详情|
|» data|object|true|none||查询数据|
|»» columns|null|true|none||键值|
|»» values|null|true|none||值域|
|»» results|[object]|true|none||查询详情|
|»»» exceptionType|string|false|none||none|
|»»» deviceId|string|false|none||none|
|»»» issueId|string|false|none||none|
|»»» crashId|string|false|none||none|
|»»» user|string|false|none||none|
|»»» hardware|string|false|none||none|
|»»» model|string|false|none||none|
|» cost|integer|true|none||查询耗时|

## POST 根据issue获取时间段crashHash列表

POST /env/uniform/openapi/getCrashDeviceInfo/platformId/platformId

根据issue获取时间段crashHash列表

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getCrashDeviceInfo.py

> Body 请求参数

```json
{
  "requestid": "",
  "stime": "",
  "etime": "",
  "source": 0,
  "filters": {
    "issueId": ""
  },
  "limit": 0,
  "type": "",
  "appId": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 是 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» source|body|integer| 否 ||环境参数|
|» filters|body|object| 否 ||筛选条件|
|»» issueId|body|string| 否 ||问题列表|
|» limit|body|integer| 否 ||返回条数|
|» type|body|string| 否 ||返回格式|
|» appId|body|string| 是 ||项目appid|

> 返回示例

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": "null",
    "values": null,
    "results": {
      "issueId": "53697147EAB75800C7B297549E31EF61",
      "crashTime": "2021-11-26 20:52:10 354",
      "crashId": "3C96296D4312F12ACAF6DEBFC22443AB",
      "user": "597862998"
    }
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||请求id|
|» code|integer|true|none||状态码|
|» errmsg|string|true|none||错误详情|
|» data|object|true|none||查询数据|
|»» columns|null|true|none||键值|
|»» values|null|true|none||值域|
|»» results|[object]|true|none||查询详情|
|»»» keyName|string|false|none||none|
|»»» model|string|false|none||none|
|»»» osVersion|string|false|none||none|
|»»» crashNums|integer|false|none||none|
|»»» crashUsers|integer|false|none||none|
|» cost|integer|true|none||查询耗时|

## POST 根据设备id获取OpenId

POST /env/uniform/openapi/getDeviceUserInfo

根据设备id获取Openid

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/openapi/crashsight_openapi_v1_getDeviceUserInfo.py

> Body 请求参数

```json
{
  "requestid": "",
  "stime": "",
  "etime": "",
  "source": 0,
  "filters": {},
  "deviceId": "",
  "limit": 0,
  "type": "",
  "appId": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 否 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» source|body|integer| 否 ||环境参数|
|» filters|body|object| 否 ||筛选条件|
|» deviceId|body|string| 否 ||设备列表|
|» limit|body|integer| 否 ||返回条数|
|» type|body|string| 否 ||返回格式|
|» appId|body|string| 是 ||项目appid|

> 返回示例

> 200 Response

```json
{
  "requestid": "string",
  "code": 0,
  "errmsg": "string",
  "data": {
    "columns": [
      "string"
    ],
    "values": [
      [
        "string"
      ]
    ],
    "results": null
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||请求id|
|» code|integer|true|none||请求id|
|» errmsg|string|true|none||错误详情|
|» data|object|true|none||查询数据|
|»» columns|[string]|true|none||键值|
|»» values|[array]|true|none||值域|
|»» results|null|true|none||查询详情|
|» cost|integer|true|none||查询耗时|

## GET 获取某一个issue下的note

GET /env/uniform/openapi/noteList

获取某一个issue下的note

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_noteList.py

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|appId|query|string| 是 ||产品id|
|platformId|query|string| 是 ||平台id,1是安卓,2是ios|
|issueId	|query|string| 是 ||问题id|
|crashDataType	|query|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "appId": "string",
  "platformId": 0,
  "issueIds": "string",
  "note": "string",
  "createTime": "string",
  "userId": "string",
  "newUserId": "string",
  "issueStatus": 0,
  "processors": "string",
  "tapdId": "string",
  "bugUrl": "string",
  "workspaceId": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||项目id|
|» platformId|integer|true|none||平台id|
|» issueIds|string|true|none||问题id|
|» note|string|true|none||备注|
|» createTime|string|true|none||发生时间|
|» userId|string|true|none||用户id|
|» newUserId|string|true|none||用户id|
|» issueStatus|integer|true|none||issue状态|
|» processors|string|true|none||处理人|
|» tapdId|string|true|none||none|
|» bugUrl|string|true|none||tapd连接|
|» workspaceId|string|true|none||tapd_workspaceId|

## POST 获取某一个issue下的note

POST /env/uniform/openapi/noteList

获取某一个issue下的note

> Body 请求参数

```json
{
  "appId": "string",
  "platformId": "string",
  "issueId": "string",
  "crashDataType": "string",
  "fsn": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||none|
|» platformId|body|string| 是 ||none|
|» issueId|body|string| 是 ||none|
|» crashDataType|body|string| 是 ||none|
|» fsn|body|string| 否 ||none|

> 返回示例

```json
{
  "appId": "3729de3c06",
  "platformId": 1,
  "issueIds": "FFF4396D2D997551BC883550B74541B2",
  "note": "mike",
  "createTime": "2021-06-25 09:56:16",
  "userId": "512466",
  "newUserId": "",
  "issueStatus": 3,
  "processors": "",
  "tapdId": "",
  "bugUrl": "",
  "workspaceId": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||none|
|» platformId|integer|true|none||none|
|» issueIds|string|true|none||none|
|» note|string|true|none||none|
|» createTime|string|true|none||none|
|» userId|string|true|none||none|
|» newUserId|string|true|none||none|
|» issueStatus|integer|true|none||none|
|» processors|string|true|none||none|
|» tapdId|string|true|none||none|
|» bugUrl|string|true|none||none|
|» workspaceId|string|true|none||none|

## GET  获取issue详情

GET /env/uniform/openapi/issueInfo/appId/{appId}/platformId/{platformId}/issueId/{issueId}

获取issue详情

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|appId|path|string| 是 ||产品id|
|platformId|path|string| 是 ||平台id,1是安卓,2是ios|
|issueId|path|string| 是 ||问题id|

> 返回示例

```json
{
  "issueId": "E91CFDD6B0ADF329B3DFC7C7EE0ED952",
  "exceptionName": "SIGILL(ILL_ILLOPC)",
  "exceptionMessage": "",
  "keyStack": "#00 pc 0000000002f0248c libUE4.so Reset (D:/SA_Client\\SA\\branches\\obt\\UE4Engine\\Engine\\Source\\Runtime\\Core\\Public\\Containers/SparseArray.h:254) [arm64-v8a]",
  "lastestUploadTime": "2021-06-15 11:54:36 199",
  "platformId": 1,
  "latestUploadTimestamp": 0,
  "imeiCount": 1,
  "sysImeiCount": 0,
  "count": 1,
  "sysCount": 0,
  "version": "#$cv#$",
  "tagInfoList": [],
  "processor": "",
  "status": 0,
  "firstUploadTime": "2021-06-15 11:54:36 199",
  "firstUploadTimestamp": 1623729276199,
  "issueHash": "E9:1C:FD:D6:B0:AD:F3:29:B3:DF:C7:C7:EE:0E:D9:52",
  "ftName": "",
  "issueVersions": [
    {
      "version": "1.0.1.10002",
      "firstUploadTime": "2021-06-15 11:54:36 199",
      "firstUploadTimestamp": 0,
      "lastUploadTime": "2021-06-15 11:54:36 199",
      "lastUploadTimestamp": 0,
      "count": 1,
      "deviceCount": 1
    }
  ],
  "detailId": "",
  "parentHash": "",
  "bugs": null
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» issueId|string|true|none||问题id|
|» exceptionName|string|true|none||异常名称|
|» exceptionMessage|string|true|none||异常信息|
|» keyStack|string|true|none||堆栈信息|
|» lastestUploadTime|string|true|none||最近上报时间|
|» platformId|integer|true|none||平台id|
|» latestUploadTimestamp|integer|true|none||none|
|» imeiCount|integer|true|none||none|
|» sysImeiCount|integer|true|none||none|
|» count|integer|true|none||发生次数|
|» sysCount|integer|true|none||none|
|» version|string|true|none||none|
|» tagInfoList|[string]|true|none||标签列表|
|» processor|string|true|none||none|
|» status|integer|true|none||none|
|» firstUploadTime|string|true|none||none|
|» firstUploadTimestamp|integer|true|none||none|
|» issueHash|string|true|none||none|
|» ftName|string|true|none||none|
|» issueVersions|[object]|true|none||issueVersions|
|»» version|string|false|none||none|
|»» firstUploadTime|string|false|none||none|
|»» firstUploadTimestamp|integer|false|none||none|
|»» lastUploadTime|string|false|none||none|
|»» lastUploadTimestamp|integer|false|none||none|
|»» count|integer|false|none||发生次数|
|»» deviceCount|integer|false|none||影响设备数|
|» detailId|string|true|none||none|
|» parentHash|string|true|none||none|
|» bugs|null|true|none||none|

## GET 根据issue获取最近一次crashHash(支持PC)

GET /env/uniform/openapi/lastCrashInfo

根据issue获取最近一次crashHash(支持PC)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：（移动端）https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_lastCrashInfo.py

（PC端）https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_lastCrashInfo%28pc%29.py

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|appId|query|string| 是 ||项目id|
|platformId|query|string| 是 ||平台id|
|issues|query|string| 是 ||issueid|
|crashDataType|query|string| 是 ||可写死|
|fsn|query|string| 否 ||可写死|

> 返回示例

```json
{
  "userId": "null",
  "processName": "com.tencent.bugly.demo.buglyqq",
  "threadName": "Thread-221(221)",
  "crashId": "A2844950BA6B2A2D9F42EBC2F1F64E77",
  "crashHash": "A2:84:49:50:BA:6B:2A:2D:9F:42:EB:C2:F1:F6:4E:77",
  "crashTime": "2020-05-07 18:36:48",
  "uploadTime": "2021-06-11 13:20:12",
  "bundleId": "com.tencent.bugly.demo.buglyqq",
  "productVersion": "1.0.3",
  "startTime": "1588837884696",
  "appInBack": "false",
  "hardware": "魅族 M6",
  "modelOriginalName": "魅族 M6",
  "osVersion": "Android 4.4.2,level 20",
  "rom": "fail%2Ffail",
  "cpuName": "fail",
  "cpuType": "i686",
  "type": "100",
  "callStack": "2020507Test4",
  "retraceCrashDetail": "2020507Test4",
  "gpuName": "null",
  "dumpId": "null",
  "new_dumpid": "null",
  "mac": "null",
  "launchTime": 9924
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» userId|string|true|none||none|
|» processName|string|true|none||none|
|» threadName|string|true|none||none|
|» crashId|string|true|none||none|
|» crashHash|string|true|none||none|
|» crashTime|string|true|none||none|
|» uploadTime|string|true|none||none|
|» bundleId|string|true|none||none|
|» productVersion|string|true|none||none|
|» startTime|string|true|none||none|
|» appInBack|string|true|none||none|
|» hardware|string|true|none||none|
|» modelOriginalName|string|true|none||none|
|» osVersion|string|true|none||none|
|» rom|string|true|none||none|
|» cpuName|string|true|none||none|
|» cpuType|string|true|none||none|
|» type|string|true|none||none|
|» callStack|string|true|none||none|
|» retraceCrashDetail|string|true|none||none|
|» gpuName|string|true|none||none|
|» dumpId|string|true|none||none|
|» new_dumpid|string|true|none||none|
|» mac|string|true|none||none|
|» launchTime|integer|true|none||none|

## POST 根据issue获取最近一次crashHash(支持PC)

POST /env/uniform/openapi/lastCrashInfo

> Body 请求参数

```json
{
  "appId": "string",
  "platformId": "string",
  "issues": "string",
  "crashDataType": "string",
  "fsn": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||none|
|» platformId|body|string| 是 ||none|
|» issues|body|string| 是 ||none|
|» crashDataType|body|string| 是 ||none|
|» fsn|body|string| 否 ||none|

> 返回示例

> 200 Response

```json
{
  "userId": "string",
  "processName": "string",
  "threadName": "string",
  "crashId": "string",
  "crashHash": "string",
  "crashTime": "string",
  "uploadTime": "string",
  "bundleId": "string",
  "productVersion": "string",
  "startTime": "string",
  "appInBack": "string",
  "hardware": "string",
  "modelOriginalName": "string",
  "osVersion": "string",
  "rom": "string",
  "cpuName": "string",
  "cpuType": "string",
  "type": "string",
  "callStack": "string",
  "retraceCrashDetail": "string",
  "gpuName": "string",
  "dumpId": "string",
  "new_dumpid": "string",
  "mac": "string",
  "launchTime": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» userId|string|true|none||none|
|» processName|string|true|none||none|
|» threadName|string|true|none||none|
|» crashId|string|true|none||none|
|» crashHash|string|true|none||none|
|» crashTime|string|true|none||none|
|» uploadTime|string|true|none||none|
|» bundleId|string|true|none||none|
|» productVersion|string|true|none||none|
|» startTime|string|true|none||none|
|» appInBack|string|true|none||none|
|» hardware|string|true|none||none|
|» modelOriginalName|string|true|none||none|
|» osVersion|string|true|none||none|
|» rom|string|true|none||none|
|» cpuName|string|true|none||none|
|» cpuType|string|true|none||none|
|» type|string|true|none||none|
|» callStack|string|true|none||none|
|» retraceCrashDetail|string|true|none||none|
|» gpuName|string|true|none||none|
|» dumpId|string|true|none||none|
|» new_dumpid|string|true|none||none|
|» mac|string|true|none||none|
|» launchTime|integer|true|none||none|

## POST 崩溃分析，ANR分析，错误分析(支持PC)

POST /env/uniform/openapi/queryIssueList

崩溃分析，ANR分析，错误分析(支持PC)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_queryIssueList.py

> Body 请求参数

```json
{
  "appId": "",
  "platformId": 0,
  "pid": "1",
  "rows": 10,
  "exceptionTypeList": "Crash,Native",
  "sortOrder": "desc",
  "status": "0,2",
  "sortField": "uploadTime",
  "issueUploadTimeRelativeMillis": 3600000,
  "date": "（此字段已废弃，改用issueUploadTimeRelativeMillis）。不传这个字段就是所有时间\n last_1_hour(最近1小时) \nlast_2_day(最近2天)\n last_7_day(最近7天) \nlast_15_day(最近15天) \nlast_30_day(最近30天)"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品ID|
|» platformId|body|integer| 是 ||平台类型，安卓端：1，iOS端：2，PC端：10|
|» pid|body|string| 是 ||平台类型，安卓端：1，iOS端：2，PC端：10|
|» rows|body|integer| 否 ||获取条数|
|» exceptionTypeList|body|string| 是 ||异常类型数组，逗号分隔多个值。支持的异常类型有：Crash, Native, AllCatched, ANR, Unity3D, AllCrash, ExtensionCrash, Lua, JS|
|» sortOrder|body|string| 是 ||排序顺序。可选值：desc, asc|
|» status|body|string| 否 ||可选，按照问题处理状态过滤 0：未处理 1： 已处理 2： 处理中 支持多选，用英文逗号连接，例如 0,2 表示过滤未处理或处理中 参数示例： 0|
|» sortField|body|string| 是 ||排序字段|
|» date|body|string| 否 ||按照问题最近时间段过滤。此字段已废弃，使用issueUploadTimeRelativeMillis替代。|
|» issueUploadTimeRelativeMillis|body|number| 是 ||按照问题的最近上报时间过滤问题。单位是毫秒，表示过滤最近上报时间在n毫秒以内的问题。例如传值3600000，表示过滤最近1小时内有过上报的问题。（注意参与过滤的属性是问题的最近上报时间，而不是上报的时间）|
|» issueFirstUploadTimeBeginMillis|body|number| 否 ||可选，格式是毫秒时间戳。按照“问题首次上报时间”来过滤返回结果。只有首次上报时间大于指定值的问题才会返回。|
|» issueFirstUploadTimeEndMillis|body|number| 否 ||可选，格式是毫秒时间戳。按照“问题首次上报时间”来过滤返回结果。只有首次上报时间小于指定值的问题才会返回。|
|» version|body|string| 否 ||多版本通过分号分隔，支持通配符*|

> 返回示例

```json
{
  "appId": "a81f9c7e38",
  "platformId": "1",
  "issueList": {
    "crashNum": 1184,
    "exceptionName": "java.lang.RuntimeException",
    "exceptionMessage": "sNSXTvFGp6ZGrorljP6WPxsGtKc5px",
    "keyStack": "",
    "lastestUploadTime": "2021-04-09 20:21:25 663",
    "issueId": "4273 DBD3409C2783706F3F15E140F25A",
    "imeiCount": 596,
    "processor": "",
    "status": 0,
    "tagInfoList": "[]",
    "count": 1184,
    "version": "#$cv#$",
    "ftName": "",
    "issueVersions": {
      "version": "3.2.5",
      "firstUploadTime": "null",
      "firstUploadTimestamp": 0,
      "lastUploadTime": null,
      "lastUploadTimestamp": 0,
      "count": 0,
      "deviceCount": 0
    }
  },
  "numFound": 1
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» appId|string|true|none||项目id|
|» platformId|string|true|none||平台id|
|» issueList|object|true|none||issuse列表|
|»» crashNum|integer|true|none||崩溃次数|
|»» exceptionName|string|true|none||异常名字|
|»» exceptionMessage|string|true|none||异常消息|
|»» keyStack|string|true|none||堆栈信息|
|»» lastestUploadTime|string|true|none||最近一次上报时间|
|»» issueId|integer|true|none||问题id|
|»» imeiCount|integer|true|none||影响设备|
|»» processor|string|true|none||issue处理人|
|»» status|integer|true|none||issue状态|
|»» tagInfoList|string|true|none||标签信息列表|
|»» count|integer|true|none||发生次数|
|»» version|string|true|none||none|
|»» ftName|string|true|none||none|
|»» issueVersions|object|true|none||子issue版本|
|»»» version|string|true|none||none|
|»»» firstUploadTime|string|true|none||none|
|»»» firstUploadTimestamp|integer|true|none||none|
|»»» lastUploadTime|null|true|none||none|
|»»» lastUploadTimestamp|integer|true|none||none|
|»»» count|integer|true|none||none|
|»»» deviceCount|integer|true|none||none|
|» numFound|integer|true|none||崩溃总数|

## GET TOP问题列表

GET /env/uniform/openapi/getTopIssue

TOP问题列表

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getTopIssue.py

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|appId|query|string| 是 ||产品id|
|platformId|query|string| 是 ||平台id|
|version|query|string| 是 ||项目版本,-1代表全版本|
|date|query|string| 是 ||YYMMDD|
|type|query|string| 是 ||三种类型-crash,anr,error|
|limit|query|string| 是 ||行数限制，获取多少行|
|topIssueDataType|query|string| 是 ||系统退出关键字分为两种情况，值为SystemExit和unSystemExit，代表匹配到系统退出关键字，未匹配到系统退出关键字|
|fsn|query|string| 是 ||fsn值可以写死|

> 返回示例

> 200 Response

```json
{
  "versionCrashUser": 0,
  "preDayVersionCrashUser": 0,
  "topIssueList": [
    {
      "appId": "string",
      "platformId": 0,
      "version": "string",
      "date": "string",
      "type": "string",
      "issueId": "string",
      "firstUploadTime": "string",
      "crashUser": 0,
      "crashNum": 0,
      "accumulateCrashNum": 0,
      "accumulateCrashUser": 0,
      "state": "string",
      "processors": "string",
      "exceptionName": "string",
      "exceptionMessage": "string",
      "keyStack": "string",
      "lastUpdateTime": "string",
      "issueVersions": [
        "string"
      ],
      "preDayCrashUser": 0,
      "preDayCrashNum": 0,
      "is_system_exit": true,
      "tags": [
        "string"
      ]
    }
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» versionCrashUser|integer|true|none||影响设备数量|
|» preDayVersionCrashUser|integer|true|none||前一天影响设备数量|
|» topIssueList|[object]|true|none||none|
|»» appId|string|false|none||产品id|
|»» platformId|integer|false|none||平台id|
|»» version|string|false|none||项目版本|
|»» date|string|false|none||时间|
|»» type|string|false|none||类型|
|»» issueId|string|false|none||问题issueId|
|»» firstUploadTime|string|false|none||首次上报时间|
|»» crashUser|integer|false|none||影响设备数|
|»» crashNum|integer|false|none||发生次数|
|»» accumulateCrashNum|integer|false|none||累计影响次数|
|»» accumulateCrashUser|integer|false|none||累计影响设备|
|»» state|string|false|none||处理状态|
|»» processors|string|false|none||处理人|
|»» exceptionName|string|false|none||异常类型|
|»» exceptionMessage|string|false|none||异常信息|
|»» keyStack|string|false|none||堆栈信息|
|»» lastUpdateTime|string|false|none||最近更新时间|
|»» issueVersions|[string]|false|none||issue版本集合|
|»» preDayCrashUser|integer|false|none||累计影响次数|
|»» preDayCrashNum|integer|false|none||累计影响设备|
|»» is_system_exit|boolean|false|none||是否系统退出|
|»» tags|[string]|false|none||标签集合|

## POST TOP问题列表(新版)

POST /uniform/openapi/getTopIssueEx

TOP问题列表

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getTopIssueEx.py

> Body 请求参数

```json
{
  "appId": "7786d1a114",
  "platformId": 1,
  "version": "-1",
  "date": "20230707",
  "type": "crash",
  "limit": 20,
  "topIssueDataType": "unSystemExit",
  "fsn": "c678c193-7a28-47c6-87aa-b79007152b97",
  "mergeMultipleVersionsWithInaccurateResult": false,
  "countryList": "",
  "versionList": [
    "1.0.0",
    "2.0.0",
    "3.0.*"
  ],
  "mergeMultipleDatesWithInaccurateResult": false,
  "minDate": "20230706",
  "maxDate": "20230708"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品id|
|» platformId|body|integer| 是 ||平台id|
|» version|body|string| 是 ||项目版本,-1代表全版本。和versionList字段二选一。如果要查询多版本，使用versionList字段。|
|» date|body|string| 是 ||YYYYMMDD格式。仅在查询单日数据时使用，查询多日使用minDate和maxDate取代此字段。|
|» type|body|string| 是 ||三种类型-crash,anr,error|
|» limit|body|integer| 是 ||行数限制，获取多少行|
|» topIssueDataType|body|string| 是 ||系统退出关键字分为两种情况，值为SystemExit和unSystemExit，代表匹配到系统退出关键字，未匹配到系统退出关键字|
|» fsn|body|string| 是 ||fsn值可以写死|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| 是 ||多版本查询结果（设备数、次数）直接相加合并。如果要查多版本必须要设置为true|
|» countryList|body|string| 是 ||国家列表|
|» versionList|body|[string]| 是 ||和version字段二选一。指定一个或多个项目版本，支持*通配符。查询多版本必须设置mergeMultipleVersionsWithInaccurateResult为true|
|» mergeMultipleDatesWithInaccurateResult|body|boolean| 是 ||是否查询多日数据（多日的设备数相加合并之后取top）|
|» minDate|body|string| 是 ||查询多日数据的时候使用，指定日期范围起点（包含）。YYYYMMDD格式|
|» maxDate|body|string| 是 ||查询多日数据的时候使用，指定日期范围终点（包含）。YYYYMMDD格式|

> 返回示例

```json
{
  "status": 200,
  "data": {
    "topIssueList": [
      {
        "appId": "b9642894f1",
        "platformId": 1,
        "date": "20230825",
        "type": "crash",
        "issueId": "63F9DDC53D9343F4B884092B49832A61",
        "firstUploadTime": "2022-03-31 22:38:14 152",
        "crashUser": 83,
        "crashNum": 83,
        "accumulateCrashNum": 123205,
        "accumulateCrashUser": 123089,
        "state": 1,
        "processors": "13cb4423f7f014cb6ba25eb359fe617a;fe8e00dd852b4cc60731fbbc0158436e;18310c25f92c4636f78d291e3d66dd2e;324c0ec5fe73b0c6975638a85ebf0773;0cdf9f01a2d74948c95056e98401982f",
        "exceptionName": "java.lang.RuntimeException",
        "exceptionMessage": "SRdSbQ3h0XOjLF90pGHvwCu5vZBLwl",
        "keyStack": "",
        "lastUpdateTime": "2023-08-25 10:24:46 395",
        "issueVersions": [
          {
            "version": "1.0.3",
            "firstUploadTime": "2022-03-31 22:38:14 152",
            "firstUploadTimestamp": 1648737494152,
            "lastUploadTime": "2023-08-25 10:24:46 395",
            "lastUploadTimestamp": 1648737494152,
            "count": 123991,
            "deviceCount": 123874,
            "systemExitCount": 0,
            "systemExitDeviceCount": 0
          }
        ],
        "preDayCrashUser": 109,
        "preDayCrashNum": 109,
        "prevHourCrashDevices": 0,
        "is_system_exit": "false",
        "tags": [
          {
            "tagId": 736,
            "tagType": 0,
            "tagCount": 0,
            "tagName": "ad"
          }
        ],
        "bugs": [
          {
            "id": "",
            "title": "",
            "workspaceId": ""
          }
        ]
      }
    ],
    "crashDevices": 0,
    "accessDevices": 0,
    "prevDayCrashDevices": 0,
    "prevDayAccessDevices": 0
  },
  "message": "OK"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||响应状态|
|» data|object|true|none||查询结果|
|»» topIssueList|[object]|true|none||none|
|»»» appId|string|false|none||产品id|
|»»» platformId|integer|false|none||平台id|
|»»» date|string|false|none||时间：YYYYMMDD|
|»»» type|string|false|none||类型|
|»»» issueId|string|false|none||问题issueId|
|»»» firstUploadTime|string|false|none||首次上报时间|
|»»» crashUser|integer|false|none||影响设备数|
|»»» crashNum|integer|false|none||发生次数|
|»»» accumulateCrashNum|integer|false|none||累计影响次数|
|»»» accumulateCrashUser|integer|false|none||累计影响设备|
|»»» state|integer|false|none||处理状态|
|»»» processors|string|false|none||处理人|
|»»» exceptionName|string|false|none||异常类型|
|»»» exceptionMessage|string|false|none||异常信息|
|»»» keyStack|string|false|none||堆栈信息|
|»»» lastUpdateTime|string|false|none||最近更新时间|
|»»» issueVersions|[object]|false|none||issue版本集合|
|»»»» version|string|false|none||版本号|
|»»»» firstUploadTime|string|false|none||首次上报时间|
|»»»» firstUploadTimestamp|integer|false|none||首次上报时间戳|
|»»»» lastUploadTime|string|false|none||最近上报时间|
|»»»» lastUploadTimestamp|integer|false|none||最近上报时间戳|
|»»»» count|integer|false|none||发生次数|
|»»»» deviceCount|integer|false|none||设备数|
|»»»» systemExitCount|integer|false|none||系统退出次数|
|»»»» systemExitDeviceCount|integer|false|none||系统退出设备数|
|»»» preDayCrashUser|integer|false|none||前一天影响设备，多日数据查询时不支持。|
|»»» preDayCrashNum|integer|false|none||前一天影响次数，多日数据查询时不支持。|
|»»» prevHourCrashDevices|integer|false|none||上一小时崩溃设备，多日数据查询时不支持。|
|»»» is_system_exit|string|false|none||是否系统退出|
|»»» tags|[object]|false|none||none|
|»»»» tagId|integer|false|none||none|
|»»»» tagType|integer|false|none||none|
|»»»» tagCount|integer|false|none||none|
|»»»» tagName|string|false|none||none|
|»»» bugs|[object]|false|none||问题单详情列表|
|»»»» id|string|false|none||tapd bug单id|
|»»»» title|string|false|none||提单时的bug单标题|
|»»»» workspaceId|string|false|none||tapd workspace id|
|»» crashDevices|integer|true|none||崩溃设备数|
|»» accessDevices|integer|true|none||联网设备数|
|»» prevDayCrashDevices|integer|true|none||前一天崩溃设备数，多日数据查询时不支持。|
|»» prevDayAccessDevices|integer|true|none||前一天联网设备数，多日数据查询时不支持。|
|» message|string|true|none||错误详情|

## POST 上报详情条件查询

POST /env/uniform/openapi/queryCrashList

上报详情条件查询

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_queryCrashList.py

> Body 请求参数

```json
{
  "appId": "f4f1ae20c0",
  "platformId": 1,
  "rows": 10,
  "start": "0",
  "sortField": "crashTime",
  "desc": true,
  "searchConditionGroup": {
    "conditions": [
      {
        "field": "version"
      },
      {
        "field": "crashUploadTime",
        "queryType": "RANGE_RELATIVE_DATETIME",
        "gte": 604800000
      },
      {
        "field": "crashDetail"
      }
    ]
  }
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品ID|
|» platformId|body|integer| 是 ||平台类型，安卓端：1，iOS端：2，PC端：10|
|» rows|body|integer| 否 ||结果分页用，设置一页的结果条数，类似于mysql的limit参数|
|» start|body|string| 是 ||结果分页用，设置结果的偏移量，类似于mysql的offset参数|
|» sortField|body|string| 是 ||排序字段。不传此字段则默认按上报时间排序。|
|» desc|body|boolean| 是 ||排序的顺序，不传则默认为倒序。true表示倒序，false表示正序。|
|» searchConditionGroup|body|object| 是 ||搜索过滤条件。可以在网站页面上使用以下方法构造该字段的数据结构： 1. 通过崩溃/卡顿/错误分析界面，点开任一条问题的问题详情界面。 2. 在问题详情界面，点击 “查看更多记录”按钮，打开 更多上报记录 页面。 3. 在更多上报记录页面的上报搜索框中，输入想要构造的搜索条件。 4. 鼠标右键点击“搜索”按钮，在弹出的气泡菜单中选择“复制过滤器的JSON数据结构（Open API用）"选项，这时搜索用的数据结构searchConditionGroup的JSON格式内容就复制到了剪贴板上。|
|»» conditions|body|[object]| 是 ||none|
|»»» field|body|string| 是 ||version  版本  |

#### 详细说明

**» sortField**: 排序字段。不传此字段则默认按上报时间排序。
uploadTime  上报时间
crashTime     崩溃发生时间

**»»» field**: version  版本  
crashUploadTime   上报时间

> 返回示例

```json
[
  {
    "status": 200,
    "ret": {
      "statusCode": 0,
      "reqSendTimestamp": 0,
      "rspReceivedTimestamp": 0,
      "rspSendTimestamp": 0,
      "numFound": 1821077,
      "issueList": [],
      "crashIdList": [
        "C67D44687F1FCDD78C5FAE006DFF3A84",
        "1581ED9E5C6A09526C9140888E450481",
        "F6B170AFF86F8668054216661D92B9E4",
        "4E9624F563918220981B623724FF85D3",
        "DC7A305DBC21FC638D0471625238C29F",
        "CD46FB5379BA92406E1E990733206F9E",
        "BEB04334EB1D60606427DC2EACCC75EB",
        "51D65EF8BE64377ECB02FD5181818655",
        "CFA8E1268A21FC9AD2BB4A560A8C1C39",
        "BD7142B162D75B1A28C8CABC5D73C1E4"
      ],
      "crashDatas": {
        "F6B170AFF86F8668054216661D92B9E4": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-48-1258344700/cos/F6B170AFF86F8668054216661D92B9E4.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "F6B170AFF86F8668054216661D92B9E4",
          "crashHash": "F6B170AFF86F8668054216661D92B9E4",
          "crashTime": "2024-05-17 19:55:51",
          "crashTimestamp": 1715946951910,
          "deviceId": "23DAFD60-082F-4704-89C6-B3F0E9927FFA",
          "diskSize": "63894048768",
          "elapsedTime": 10714500344,
          "expAddr": "",
          "expMessage": "UpdaterExceedMaxFileDownloadTimesBeforeAuth",
          "expName": "UpdaterExceedMaxFileDownloadTimesBeforeAuth",
          "expUid": "1F72E004-7BA6-4347-AFE6-20A559B8390F",
          "freeMem": "692994048",
          "freeSdCard": "0",
          "freeStorage": "253748688",
          "hardware": "iPhone X GSM",
          "hasLogFile": false,
          "id": "F6B170AFF86F8668054216661D92B9E4",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "96A9753EC924B89461BE49FB2E39C431",
          "memSize": "2961539072",
          "model": "iPhone X GSM",
          "modelOriginalName": "iphone10,6",
          "osVer": "16.6.1 (20G81)",
          "osVersion": "16.6.1 (20G81)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 20:02:36",
          "uploadTimestamp": 1705233756295,
          "userId": "Unknown",
          "featureTagInfos": []
        },
        "BEB04334EB1D60606427DC2EACCC75EB": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-3-1258344700/cos/BEB04334EB1D60606427DC2EACCC75EB.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "BEB04334EB1D60606427DC2EACCC75EB",
          "crashHash": "BEB04334EB1D60606427DC2EACCC75EB",
          "crashTime": "2024-03-27 11:02:06",
          "crashTimestamp": 1711508526696,
          "deviceId": "A50B9AB9-817C-4AC4-A837-B44D2D4EF5C7",
          "diskSize": "31989469184",
          "elapsedTime": 8401,
          "expAddr": "",
          "expMessage": "BeforeAuthPakSizeCheckError",
          "expName": "BeforeAuthPakSizeCheckError",
          "expUid": "4BE6BAD7-7974-466D-B9C1-5309532758D1",
          "freeMem": "1146830848",
          "freeSdCard": "0",
          "freeStorage": "4613673752",
          "hardware": "iPhone 7 Plus (9,2)",
          "hasLogFile": false,
          "id": "BEB04334EB1D60606427DC2EACCC75EB",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "699A825C8A489C59CE5FBF5FC3B2DF9B",
          "memSize": "3145728000",
          "model": "iPhone 7 Plus (9,2)",
          "modelOriginalName": "iphone9,2",
          "osVer": "13.4.1 (17E262)",
          "osVersion": "13.4.1 (17E262)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 11:04:06",
          "uploadTimestamp": 1705201446715,
          "userId": "Unknown",
          "featureTagInfos": []
        },
        "CD46FB5379BA92406E1E990733206F9E": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-82-1258344700/cos/CD46FB5379BA92406E1E990733206F9E.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "CD46FB5379BA92406E1E990733206F9E",
          "crashHash": "CD46FB5379BA92406E1E990733206F9E",
          "crashTime": "2024-03-27 11:02:06",
          "crashTimestamp": 1711508526697,
          "deviceId": "A50B9AB9-817C-4AC4-A837-B44D2D4EF5C7",
          "diskSize": "31989469184",
          "elapsedTime": 8402,
          "expAddr": "",
          "expMessage": "BeforeAuthPakSizeCheckError",
          "expName": "BeforeAuthPakSizeCheckError",
          "expUid": "3EA7D5D1-8F31-422D-8FE3-1D8DDABFEC5D",
          "freeMem": "1146830848",
          "freeSdCard": "0",
          "freeStorage": "4613317400",
          "hardware": "iPhone 7 Plus (9,2)",
          "hasLogFile": false,
          "id": "CD46FB5379BA92406E1E990733206F9E",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "699A825C8A489C59CE5FBF5FC3B2DF9B",
          "memSize": "3145728000",
          "model": "iPhone 7 Plus (9,2)",
          "modelOriginalName": "iphone9,2",
          "osVer": "13.4.1 (17E262)",
          "osVersion": "13.4.1 (17E262)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 11:04:09",
          "uploadTimestamp": 1705201449420,
          "userId": "Unknown",
          "featureTagInfos": []
        },
        "BD7142B162D75B1A28C8CABC5D73C1E4": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-4-1258344700/cos/BD7142B162D75B1A28C8CABC5D73C1E4.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "BD7142B162D75B1A28C8CABC5D73C1E4",
          "crashHash": "BD7142B162D75B1A28C8CABC5D73C1E4",
          "crashTime": "2024-03-27 11:00:15",
          "crashTimestamp": 1711508415381,
          "deviceId": "A50B9AB9-817C-4AC4-A837-B44D2D4EF5C7",
          "diskSize": "31989469184",
          "elapsedTime": 7565,
          "expAddr": "",
          "expMessage": "BeforeAuthPakSizeCheckError",
          "expName": "BeforeAuthPakSizeCheckError",
          "expUid": "569AF4B7-0718-4A79-964F-E0A7671759A1",
          "freeMem": "1153662976",
          "freeSdCard": "0",
          "freeStorage": "4537656088",
          "hardware": "iPhone 7 Plus (9,2)",
          "hasLogFile": false,
          "id": "BD7142B162D75B1A28C8CABC5D73C1E4",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "699A825C8A489C59CE5FBF5FC3B2DF9B",
          "memSize": "3145728000",
          "model": "iPhone 7 Plus (9,2)",
          "modelOriginalName": "iphone9,2",
          "osVer": "13.4.1 (17E262)",
          "osVersion": "13.4.1 (17E262)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 11:04:06",
          "uploadTimestamp": 1705201446990,
          "userId": "Unknown",
          "featureTagInfos": []
        },
        "DC7A305DBC21FC638D0471625238C29F": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-69-1258344700/cos/DC7A305DBC21FC638D0471625238C29F.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "DC7A305DBC21FC638D0471625238C29F",
          "crashHash": "DC7A305DBC21FC638D0471625238C29F",
          "crashTime": "2024-03-30 12:12:38",
          "crashTimestamp": 1711771958490,
          "deviceId": "682DD5A9-D105-4325-9264-AA3187E4F423",
          "diskSize": "31978991616",
          "elapsedTime": 734290,
          "expAddr": "",
          "expMessage": "ConnectionWaiting_10",
          "expName": "ConnectionWaiting_10",
          "expUid": "11623D27-FB9F-4220-8115-A636A7C0DFDF",
          "freeMem": "837484544",
          "freeSdCard": "0",
          "freeStorage": "2154887160",
          "hardware": "iPhone 7 Plus (9,2)",
          "hasLogFile": false,
          "id": "DC7A305DBC21FC638D0471625238C29F",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "B95F76410E7FE07F34F1DC47F386D670",
          "memSize": "3144810496",
          "model": "iPhone 7 Plus (9,2)",
          "modelOriginalName": "iphone9,2",
          "osVer": "15.7.8 (19H364)",
          "osVersion": "15.7.8 (19H364)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 19:34:00",
          "uploadTimestamp": 1705232040895,
          "userId": "osewR0o-WuAdrL3A0U7TSwPSi7uU",
          "featureTagInfos": []
        },
        "4E9624F563918220981B623724FF85D3": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-89-1258344700/cos/4E9624F563918220981B623724FF85D3.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "4E9624F563918220981B623724FF85D3",
          "crashHash": "4E9624F563918220981B623724FF85D3",
          "crashTime": "2024-03-30 12:12:42",
          "crashTimestamp": 1711771962212,
          "deviceId": "682DD5A9-D105-4325-9264-AA3187E4F423",
          "diskSize": "31978991616",
          "elapsedTime": 738012,
          "expAddr": "",
          "expMessage": "ConnectionWaiting_Over",
          "expName": "ConnectionWaiting_Over",
          "expUid": "E1DCED42-4845-4F13-9050-D618AF318352",
          "freeMem": "834519040",
          "freeSdCard": "0",
          "freeStorage": "2154887160",
          "hardware": "iPhone 7 Plus (9,2)",
          "hasLogFile": false,
          "id": "4E9624F563918220981B623724FF85D3",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "6F0EACDAD9B85DBE19791187EA006AB1",
          "memSize": "3144810496",
          "model": "iPhone 7 Plus (9,2)",
          "modelOriginalName": "iphone9,2",
          "osVer": "15.7.8 (19H364)",
          "osVersion": "15.7.8 (19H364)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 19:34:00",
          "uploadTimestamp": 1705232040311,
          "userId": "osewR0o-WuAdrL3A0U7TSwPSi7uU",
          "featureTagInfos": []
        },
        "CFA8E1268A21FC9AD2BB4A560A8C1C39": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-79-1258344700/cos/CFA8E1268A21FC9AD2BB4A560A8C1C39.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "CFA8E1268A21FC9AD2BB4A560A8C1C39",
          "crashHash": "CFA8E1268A21FC9AD2BB4A560A8C1C39",
          "crashTime": "2024-03-27 11:00:15",
          "crashTimestamp": 1711508415382,
          "deviceId": "A50B9AB9-817C-4AC4-A837-B44D2D4EF5C7",
          "diskSize": "31989469184",
          "elapsedTime": 7566,
          "expAddr": "",
          "expMessage": "BeforeAuthPakSizeCheckError",
          "expName": "BeforeAuthPakSizeCheckError",
          "expUid": "E4D6C52F-390F-4CDF-8FA9-0C9F656E585B",
          "freeMem": "1153662976",
          "freeSdCard": "0",
          "freeStorage": "4537643800",
          "hardware": "iPhone 7 Plus (9,2)",
          "hasLogFile": false,
          "id": "CFA8E1268A21FC9AD2BB4A560A8C1C39",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "699A825C8A489C59CE5FBF5FC3B2DF9B",
          "memSize": "3145728000",
          "model": "iPhone 7 Plus (9,2)",
          "modelOriginalName": "iphone9,2",
          "osVer": "13.4.1 (17E262)",
          "osVersion": "13.4.1 (17E262)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 11:04:10",
          "uploadTimestamp": 1705201450810,
          "userId": "Unknown",
          "featureTagInfos": []
        },
        "C67D44687F1FCDD78C5FAE006DFF3A84": {
          "addCodeFrame": [
            "3,0x00000001065fd4d8",
            "6,0x0000000107d7d1e0",
            "7,0x0000000103d59eb4"
          ],
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-28-1258344700/cos/C67D44687F1FCDD78C5FAE006DFF3A84.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "C67D44687F1FCDD78C5FAE006DFF3A84",
          "crashHash": "C67D44687F1FCDD78C5FAE006DFF3A84",
          "crashTime": "2413-09-02 06:38:57",
          "crashTimestamp": 14000855937058,
          "deviceId": "E9A1C689-EDEA-4DE5-8523-0CFA5C680865",
          "diskSize": "63989469184",
          "elapsedTime": 12295692532101,
          "expAddr": "0x000000018eb59ec4",
          "expMessage": "",
          "expName": "SIGABRT",
          "expUid": "BB1F6E7C-6891-42B0-B0BE-6B10B158E632",
          "freeMem": "1226391552",
          "freeSdCard": "0",
          "freeStorage": "37405688829",
          "hardware": "iPhone 8 Plus (10,2)",
          "hasLogFile": false,
          "id": "C67D44687F1FCDD78C5FAE006DFF3A84",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "761A39027EF54813036BB11BDD98BEF9",
          "memSize": "3116498944",
          "model": "iPhone 8 Plus (10,2)",
          "modelOriginalName": "iphone10,2",
          "osVer": "13.3 (17C54)",
          "osVersion": "13.3 (17C54)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "3 ",
          "totalSD": "0",
          "type": "100",
          "uploadTime": "2024-01-14 00:48:07",
          "uploadTimestamp": 1705164487910,
          "userId": "osewR0txvXlV8rtX8bujSpCsAqQE",
          "featureTagInfos": []
        },
        "1581ED9E5C6A09526C9140888E450481": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-37-1258344700/cos/1581ED9E5C6A09526C9140888E450481.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "1581ED9E5C6A09526C9140888E450481",
          "crashHash": "1581ED9E5C6A09526C9140888E450481",
          "crashTime": "2025-01-17 16:04:27",
          "crashTimestamp": 1737101067424,
          "deviceId": "79789F22-B412-4DD2-9EB2-AD066CAB047A",
          "diskSize": "63876222976",
          "elapsedTime": 943306,
          "expAddr": "",
          "expMessage": "UpdaterExceedMaxFileDownloadTimesBeforeAuth",
          "expName": "UpdaterExceedMaxFileDownloadTimesBeforeAuth",
          "expUid": "DD2E70D1-5B3B-4373-9ED0-D3F1FD6D99AE",
          "freeMem": "1035485184",
          "freeSdCard": "0",
          "freeStorage": "1577717584",
          "hardware": "iPhone XS Max Global",
          "hasLogFile": false,
          "id": "1581ED9E5C6A09526C9140888E450481",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "96A9753EC924B89461BE49FB2E39C431",
          "memSize": "3941236736",
          "model": "iPhone XS Max Global",
          "modelOriginalName": "iphone11,6",
          "osVer": "16.1.2 (20B110)",
          "osVersion": "16.1.2 (20B110)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-17 16:36:18",
          "uploadTimestamp": 1705480578924,
          "userId": "Unknown",
          "featureTagInfos": []
        },
        "51D65EF8BE64377ECB02FD5181818655": {
          "apn": "wifi",
          "appBit": 0,
          "appInBack": "false",
          "bucketPath": "crashsight-crash-95-1258344700/cos/51D65EF8BE64377ECB02FD5181818655.zip",
          "bundleId": "com.tencent.tmgp.pubgmhd",
          "channelId": "unknown",
          "country": "",
          "countryOrRegionCode": "",
          "cpuType": "arm64-v8a",
          "crashCount": 0,
          "crashId": "51D65EF8BE64377ECB02FD5181818655",
          "crashHash": "51D65EF8BE64377ECB02FD5181818655",
          "crashTime": "2024-03-27 11:02:06",
          "crashTimestamp": 1711508526695,
          "deviceId": "A50B9AB9-817C-4AC4-A837-B44D2D4EF5C7",
          "diskSize": "31989469184",
          "elapsedTime": 8400,
          "expAddr": "",
          "expMessage": "BeforeAuthPakSizeCheckError",
          "expName": "BeforeAuthPakSizeCheckError",
          "expUid": "11F4390A-AC5E-4E73-AD4B-88374C6107EC",
          "freeMem": "1146830848",
          "freeSdCard": "0",
          "freeStorage": "4613980952",
          "hardware": "iPhone 7 Plus (9,2)",
          "hasLogFile": false,
          "id": "51D65EF8BE64377ECB02FD5181818655",
          "isRooted": "false",
          "isSystemStack": 0,
          "isVirtualMachine": 0,
          "issueId": "699A825C8A489C59CE5FBF5FC3B2DF9B",
          "memSize": "3145728000",
          "model": "iPhone 7 Plus (9,2)",
          "modelOriginalName": "iphone9,2",
          "osVer": "13.4.1 (17E262)",
          "osVersion": "13.4.1 (17E262)",
          "processName": "shadowtrackerextra",
          "productVersion": "1.25.12.12000",
          "retraceCrashDetail": "",
          "retraceStatus": 0,
          "retraceTimestamp": 0,
          "sdkVersion": "GCLOUD_VERSION_CRASHSIGHT_4.2.15.23.sgprod",
          "startTimestamp": 0,
          "threadName": "",
          "totalSD": "0",
          "type": "106",
          "uploadTime": "2024-01-14 11:04:07",
          "uploadTimestamp": 1705201447996,
          "userId": "Unknown",
          "featureTagInfos": []
        }
      },
      "crashNums": 0,
      "anrNums": 0,
      "errorNums": 0,
      "totalCrashMatchCount": 0
    }
  }
]
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|false|none||none|
|» ret|object|false|none||none|
|»» statusCode|integer|true|none||none|
|»» reqSendTimestamp|integer|true|none||none|
|»» rspReceivedTimestamp|integer|true|none||none|
|»» rspSendTimestamp|integer|true|none||none|
|»» numFound|integer|true|none||满足搜索条件的所有上报总数。|
|»» issueList|[string]|true|none||none|
|»» crashIdList|[string]|true|none||查询出的一页上报结果的crashId数组。|
|»» crashDatas|object|true|none||查询出的一页上报结果详情字典。字典的key是crashId，value是异常上报的详情。value的数据结构与crashDoc接口返回值中的crashMap字段一致。|
|»»» F6B170AFF86F8668054216661D92B9E4|object|true|none||none|
|»»»» apn|string|true|none||none|
|»»»» appBit|integer|true|none||none|
|»»»» appInBack|string|true|none||none|
|»»»» bucketPath|string|true|none||none|
|»»»» bundleId|string|true|none||none|
|»»»» channelId|string|true|none||none|
|»»»» country|string|true|none||none|
|»»»» countryOrRegionCode|string|true|none||none|
|»»»» cpuType|string|true|none||none|
|»»»» crashCount|integer|true|none||none|
|»»»» crashId|string|true|none||none|
|»»»» crashHash|string|true|none||none|
|»»»» crashTime|string|true|none||none|
|»»»» crashTimestamp|integer|true|none||none|
|»»»» deviceId|string|true|none||none|
|»»»» diskSize|string|true|none||none|
|»»»» elapsedTime|integer|true|none||none|
|»»»» expAddr|string|true|none||none|
|»»»» expMessage|string|true|none||none|
|»»»» expName|string|true|none||none|
|»»»» expUid|string|true|none||none|
|»»»» freeMem|string|true|none||none|
|»»»» freeSdCard|string|true|none||none|
|»»»» freeStorage|string|true|none||none|
|»»»» hardware|string|true|none||none|
|»»»» hasLogFile|boolean|true|none||none|
|»»»» id|string|true|none||none|
|»»»» isRooted|string|true|none||none|
|»»»» isSystemStack|integer|true|none||none|
|»»»» isVirtualMachine|integer|true|none||none|
|»»»» issueId|string|true|none||none|
|»»»» memSize|string|true|none||none|
|»»»» model|string|true|none||none|
|»»»» modelOriginalName|string|true|none||none|
|»»»» osVer|string|true|none||none|
|»»»» osVersion|string|true|none||none|
|»»»» processName|string|true|none||none|
|»»»» productVersion|string|true|none||none|
|»»»» retraceCrashDetail|string|true|none||none|
|»»»» retraceStatus|integer|true|none||none|
|»»»» retraceTimestamp|integer|true|none||none|
|»»»» sdkVersion|string|true|none||none|
|»»»» startTimestamp|integer|true|none||none|
|»»»» threadName|string|true|none||none|
|»»»» totalSD|string|true|none||none|
|»»»» type|string|true|none||none|
|»»»» uploadTime|string|true|none||none|
|»»»» uploadTimestamp|integer|true|none||none|
|»»»» userId|string|true|none||none|
|»»»» featureTagInfos|[string]|true|none||none|
|»» crashNums|integer|true|none||none|
|»» anrNums|integer|true|none||none|
|»» errorNums|integer|true|none||none|
|»» totalCrashMatchCount|integer|true|none||none|

## POST  获取issue详情

POST /env/uniform/openapi/issueInfo

> Body 请求参数

```json
{
  "appId": "string",
  "platformId": "string",
  "issueId": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||none|
|» platformId|body|string| 是 ||none|
|» issueId|body|string| 是 ||none|

> 返回示例

```json
{
  "issueId": "E91CFDD6B0ADF329B3DFC7C7EE0ED952",
  "exceptionName": "SIGILL(ILL_ILLOPC)",
  "exceptionMessage": "",
  "keyStack": "#00 pc 0000000002f0248c libUE4.so Reset (D:/SA_Client\\SA\\branches\\obt\\UE4Engine\\Engine\\Source\\Runtime\\Core\\Public\\Containers/SparseArray.h:254) [arm64-v8a]",
  "lastestUploadTime": "2021-06-15 11:54:36 199",
  "platformId": 1,
  "latestUploadTimestamp": 0,
  "imeiCount": 1,
  "sysImeiCount": 0,
  "count": 1,
  "sysCount": 0,
  "version": "#$cv#$",
  "tagInfoList": [],
  "processor": "",
  "status": 0,
  "firstUploadTime": "2021-06-15 11:54:36 199",
  "firstUploadTimestamp": 1623729276199,
  "issueHash": "E9:1C:FD:D6:B0:AD:F3:29:B3:DF:C7:C7:EE:0E:D9:52",
  "ftName": "",
  "issueVersions": [
    {
      "version": "1.0.1.10002",
      "firstUploadTime": "2021-06-15 11:54:36 199",
      "firstUploadTimestamp": 0,
      "lastUploadTime": "2021-06-15 11:54:36 199",
      "lastUploadTimestamp": 0,
      "count": 1,
      "deviceCount": 1
    }
  ],
  "detailId": "",
  "parentHash": "",
  "bugs": null
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» issueId|string|true|none||none|
|» exceptionName|string|true|none||none|
|» exceptionMessage|string|true|none||none|
|» keyStack|string|true|none||none|
|» lastestUploadTime|string|true|none||none|
|» platformId|integer|true|none||none|
|» latestUploadTimestamp|integer|true|none||none|
|» imeiCount|integer|true|none||none|
|» sysImeiCount|integer|true|none||none|
|» count|integer|true|none||none|
|» sysCount|integer|true|none||none|
|» version|string|true|none||none|
|» tagInfoList|[string]|true|none||none|
|» processor|string|true|none||none|
|» status|integer|true|none||none|
|» firstUploadTime|string|true|none||none|
|» firstUploadTimestamp|integer|true|none||none|
|» issueHash|string|true|none||none|
|» ftName|string|true|none||none|
|» issueVersions|[object]|true|none||none|
|»» version|string|false|none||none|
|»» firstUploadTime|string|false|none||none|
|»» firstUploadTimestamp|integer|false|none||none|
|»» lastUploadTime|string|false|none||none|
|»» lastUploadTimestamp|integer|false|none||none|
|»» count|integer|false|none||none|
|»» deviceCount|integer|false|none||none|
|» detailId|string|true|none||none|
|» parentHash|string|true|none||none|
|» bugs|null|true|none||none|

# 其他

## POST 创建缺陷单

POST /env/uniform/openapi/upsertBugs

创建缺陷单

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_upsertBugs.py

> Body 请求参数

```json
{
  "appId": "d98b9f7eec",
  "platformId": 1,
  "issueList": [
    {
      "issueHash": "97CF6DE03A2BCF2A517A1F3AC2A4CF77",
      "bugInfoList": [
        {
          "status": "new",
          "titleBase64": "",
          "descriptionBase64": "",
          "reporter": "demo",
          "includeAttachments": false,
          "attachmentFilenameList": [],
          "severity": "normal",
          "versionReport": "发现版本4",
          "iterationId": "1020428185001284771",
          "release_id": "",
          "currentOwner": "v_fzqfang"
        }
      ]
    }
  ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||项目ID|
|» platformId|body|integer| 是 ||平台ID： 1（安卓）2（IOS）10（PC）|
|» issueList|body|[object]| 是 ||问题列表|
|»» issueHash|body|string| 否 ||问题HASH|
|»» bugInfoList|body|[object]| 否 ||问题单详情：缺陷字段参考：https://o.tapd.woa.com/document/api-doc/API%E6%96%87%E6%A1%A3/api_reference/bug/get_bug_fields_info.html|
|»»» status|body|string| 否 ||问题单状态|
|»»» titleBase64|body|string| 否 ||问题单标题，需要base64编码|
|»»» descriptionBase64|body|string| 否 ||详细描述，需要base64编码|
|»»» reporter|body|string| 否 ||创建人（企业微信名）|
|»»» includeAttachments|body|boolean| 否 ||是否包含附件|
|»»» attachmentFilenameList|body|[string]| 否 ||附件文件列表|
|»»» severity|body|string| 否 ||严重程度|
|»»» versionReport|body|string| 否 ||发现版本|
|»»» iterationId|body|string| 否 ||迭代ID|
|»»» release_id|body|string| 否 ||发布计划|
|»»» currentOwner|body|string| 否 ||处理人（企业微信名）|
|»»» module|body|string| 否 ||模块|
|»»» testtype|body|string| 否 ||测试类型|

> 返回示例

```json
{
  "status": 200,
  "ret": 200,
  "data": [
    true
  ],
  "message": "OK"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||响应状态码|
|» ret|integer|true|none||创建结果|
|» data|[boolean]|true|none||创建状态|
|» message|string|true|none||错误详情|

## POST 更新issue状态接口

POST /env/uniform/openapi/updateIssueStatus

更新issue状态接口

国内： https://crashsight.qq.com

#新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_updateIssueStatus.py

> Body 请求参数

```json
{
  "appId": "3729de3c06",
  "issueIds": "FFF4396D2D997551BC883550B74541B2",
  "status": 2,
  "processors": "13cb4423f7f014cb6ba25eb359fe617a",
  "note": "",
  "createTime": "2023-08-22 14:43:09",
  "platformId": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品id|
|» issueIds|body|string| 是 ||问题id|
|» status|body|integer| 是 ||状态码：  0（未处理）1（已处理）2（处理中）|
|» processors|body|string| 是 ||处理人：wetest uin 可根据getSelectorDatas获取userId|
|» note|body|string| 是 ||备注|
|» createTime|body|string| 是 ||更新时间|
|» platformId|body|integer| 是 ||平台id： 1（安卓）2（IOS）10（PC）|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "“”"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||响应状态|
|» ret|object|true|none||查询结果|
|»» code|integer|true|none||查询状态码|
|»» message|string|true|none||错误详情|
|»» errorCode|string|true|none||错误代码|

## POST 根据expUid获取机型列表(移动端)

POST /env/uniform/openapi/getCrashDeviceInfoByExpUid

根据expUid获取机型列表(移动端)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/openapi/crashsight_openapi_v1_getCrashDeviceInfoByExpUid.py

> Body 请求参数

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "stime": "2022-08-30 00:00:00",
  "etime": "2022-08-31 00:00:00",
  "filters": {
    "expUid": "2f95d94c-824a-4fb3-8316-8a369fd52f09"
  },
  "limit": 0,
  "type": "pretty"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 否 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» filters|body|object| 否 ||筛选条件|
|»» expUid|body|string| 否 ||expUid列表|
|» limit|body|integer| 否 ||返回条数|
|» type|body|string| 否 ||返回条数|

> 返回示例

> 200 Response

```json
{
  "requestid": "string",
  "code": 0,
  "errmsg": "string",
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "dtEventTime": "string",
        "expUid": "string",
        "deviceId": "string",
        "device_ram": 0,
        "device_rom": 0,
        "model": "string",
        "osVer": "string"
      }
    ]
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||请求id|
|» code|integer|true|none||状态码|
|» errmsg|string|true|none||错误详情|
|» data|object|true|none||查询数据|
|»» columns|null|true|none||键值|
|»» values|null|true|none||值域|
|»» results|[object]|true|none||查询详情|
|»»» dtEventTime|string|false|none||none|
|»»» expUid|string|false|none||none|
|»»» deviceId|string|false|none||none|
|»»» device_ram|integer|false|none||none|
|»»» device_rom|integer|false|none||none|
|»»» model|string|false|none||none|
|»»» osVer|string|false|none||none|
|» cost|integer|true|none||查询耗时|

## POST 添加问题备注

POST /env/uniform/openapi/addIssueNote

添加问题备注接口

国内： https://crashsight.qq.com

#新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_addIssueNote.py

> Body 请求参数

```json
{
  "appId": "3729de3c06",
  "platformId": 1,
  "issueStatus": 3,
  "issueIds": "650C2C6DF962E9D6ACE6BF5C9F27676D",
  "note": "yyy",
  "createTime": "2023-08-22 14:51:36",
  "newUserId": "12453"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» appId|body|string| 是 ||产品ID|
|» platformId|body|integer| 是 ||平台ID： 1（安卓）2（IOS）10（PC）|
|» issueStatus|body|integer| 是 ||问题状态：3（更新状态，此接口此处固定值）|
|» issueIds|body|string| 是 ||问题id|
|» note|body|string| 是 ||备注|
|» createTime|body|string| 是 ||发生时间|
|» newUserId|body|string| 是 ||用户ID|

> 返回示例

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "“”",
    "data": true
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|integer|true|none||响应状态|
|» ret|object|true|none||查询结果|
|»» code|integer|true|none||查询状态码|
|»» message|string|true|none||错误详情|
|»» errorCode|string|true|none||错误详情|
|»» data|boolean|true|none||none|

## POST 获取系统保存的版本号首次出现的日期(个别项目通用获取使用，数据被清理时数据会变动)

POST /uniform/openapi/getVersionDateList

获取系统保存的版本号首次出现的日期(个别项目通用获取使用，数据被清理时数据会变动)

国内： https://crashsight.qq.com

#新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准

> Body 请求参数

```json
{
  "requestid": "",
  "stime": "",
  "etime": "",
  "params": {},
  "limit": 0,
  "type": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 是 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» params|body|object| 否 ||额外功能条件|
|» limit|body|integer| 否 ||返回条数(按照时间倒序）|
|» type|body|string| 否 ||返回格式 9.Json "type":"pretty" 10.默认返回值域和列值|

> 返回示例

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "dtEventTime": "-",
        "product_version": "-1",
        "first_date": "2022-10-26"
      }
    ]
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||请求id|
|» code|integer|true|none||状态码|
|» errmsg|string|true|none||错误详情|
|» data|object|true|none||查询数据|
|»» columns|null|true|none||键值|
|»» values|null|true|none||值域|
|»» results|[object]|true|none||查询详情|
|»»» dtEventTime|string|false|none||none|
|»»» product_version|string|false|none||none|
|»»» first_date|string|false|none||none|
|» cost|integer|true|none||none|

## GET 获取版本，包名，处理人等列表(支持PC)

GET /env/uniform/openapi/getSelectorDatas

获取版本，包名，处理人等列表(支持PC)

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/uniform/crashsight_openapi_v1_getSelectorDatas.py

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|appId|query|string| 是 ||项目id|
|pid|query|string| 是 ||平台id|
|fsn|query|string| 是 ||可写死|

#### 枚举值

|属性|值|
|---|---|
|pid|1|
|pid|2|
|pid|10|

> 返回示例

```json
{
  "code": 200,
  "message": "OK",
  "errorCode": "",
  "data": {
    "versionList": {
      "appId": "3729de3c06",
      "platformId": 1,
      "productVersion": "1.0.3",
      "enable": 1,
      "isShow": true,
      "enableAutoUpgrade": false,
      "sdkVersion": "3.1.7(1.6.0)-3.7.1"
    },
    "tagList": [
      {
        "appId": "3729de3c06",
        "platformId": 1,
        "tagId": 2099,
        "tagName": "哈哈哈哈哈",
        "isShow": 1
      }
    ],
    "processorList": {
      "appId": "3729de3c06",
      "platformId": 1,
      "type": 1,
      "userId": "380b6196b8bd21ed08137900a5d05816",
      "registerTime": "2020-08-31 04:40:01",
      "logoUrl": "",
      "wechat": "",
      "email": "",
      "phone": "",
      "isShow": "true",
      "qqNickName": "4648",
      "name": "terryxdguan",
      "newUserId": "4648",
      "isOperator": 0
    },
    "disableMemberInvitation": false,
    "channelList": [
      "testchannel",
      "1101"
    ],
    "bundleIdList": [
      "com.tencent.crashsight.demo.glyj",
      "com.tencent.crashsight.demo.qq"
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errorCode|string|true|none||none|
|» data|object|true|none||none|
|»» versionList|object|true|none||版本列表|
|»»» appId|string|true|none||none|
|»»» platformId|integer|true|none||none|
|»»» productVersion|string|true|none||none|
|»»» enable|integer|true|none||none|
|»»» isShow|boolean|true|none||none|
|»»» enableAutoUpgrade|boolean|true|none||none|
|»»» sdkVersion|string|true|none||none|
|»» tagList|[object]|true|none||none|
|»»» appId|string|false|none||none|
|»»» platformId|integer|false|none||none|
|»»» tagId|integer|false|none||none|
|»»» tagName|string|false|none||none|
|»»» isShow|integer|false|none||none|
|»» processorList|object|true|none||处理人列表|
|»»» appId|string|true|none||none|
|»»» platformId|integer|true|none||none|
|»»» type|integer|true|none||none|
|»»» userId|string|true|none||none|
|»»» registerTime|string|true|none||none|
|»»» logoUrl|string|true|none||none|
|»»» wechat|string|true|none||none|
|»»» email|string|true|none||none|
|»»» phone|string|true|none||none|
|»»» isShow|string|true|none||none|
|»»» qqNickName|string|true|none||none|
|»»» name|string|true|none||none|
|»»» newUserId|string|true|none||none|
|»»» isOperator|integer|true|none||none|
|»» disableMemberInvitation|boolean|true|none||none|
|»» channelList|[string]|true|none||none|
|»» bundleIdList|[string]|true|none||包名列表|

## POST 获取版本，包名，处理人等列表(支持PC)

POST /env/uniform/openapi/getSelectorDatas

> Body 请求参数

```json
{
  "appId": "string",
  "pid": "1",
  "fsn": "string",
  "types": "version,member,bundle,tag,channel"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» appId|body|string| 是 | 项目id|none|
|» pid|body|string| 是 | 平台id|none|
|» fsn|body|string| 是 | 请求id|none|
|» types|body|string| 否 ||none|

#### 枚举值

|属性|值|
|---|---|
|» pid|1|
|» pid|2|
|» pid|10|

> 返回示例

```json
{
  "code": 200,
  "message": "OK",
  "errorCode": "",
  "data": {
    "versionList": {
      "appId": "3729de3c06",
      "platformId": 1,
      "productVersion": "1.0.3",
      "enable": 1,
      "isShow": true,
      "enableAutoUpgrade": false,
      "sdkVersion": "3.1.7(1.6.0)-3.7.1"
    },
    "tagList": [
      {
        "appId": "3729de3c06",
        "platformId": 1,
        "tagId": 2099,
        "tagName": "哈哈哈哈哈",
        "isShow": 1
      }
    ],
    "processorList": {
      "appId": "3729de3c06",
      "platformId": 1,
      "type": 1,
      "userId": "380b6196b8bd21ed08137900a5d05816",
      "registerTime": "2020-08-31 04:40:01",
      "logoUrl": "",
      "wechat": "",
      "email": "",
      "phone": "",
      "isShow": "true",
      "qqNickName": "4648",
      "name": "terryxdguan",
      "newUserId": "4648",
      "isOperator": 0
    },
    "disableMemberInvitation": false,
    "channelList": [
      "testchannel",
      "1101"
    ],
    "bundleIdList": [
      "com.tencent.crashsight.demo.glyj",
      "com.tencent.crashsight.demo.qq"
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errorCode|string|true|none||none|
|» data|object|true|none||none|
|»» versionList|object|true|none||none|
|»»» appId|string|true|none||none|
|»»» platformId|integer|true|none||none|
|»»» productVersion|string|true|none||none|
|»»» enable|integer|true|none||none|
|»»» isShow|boolean|true|none||none|
|»»» enableAutoUpgrade|boolean|true|none||none|
|»»» sdkVersion|string|true|none||none|
|»» tagList|[object]|true|none||none|
|»»» appId|string|false|none||none|
|»»» platformId|integer|false|none||none|
|»»» tagId|integer|false|none||none|
|»»» tagName|string|false|none||none|
|»»» isShow|integer|false|none||none|
|»» processorList|object|true|none||none|
|»»» appId|string|true|none||none|
|»»» platformId|integer|true|none||none|
|»»» type|integer|true|none||none|
|»»» userId|string|true|none||none|
|»»» registerTime|string|true|none||none|
|»»» logoUrl|string|true|none||none|
|»»» wechat|string|true|none||none|
|»»» email|string|true|none||none|
|»»» phone|string|true|none||none|
|»»» isShow|string|true|none||none|
|»»» qqNickName|string|true|none||none|
|»»» name|string|true|none||none|
|»»» newUserId|string|true|none||none|
|»»» isOperator|integer|true|none||none|
|»» disableMemberInvitation|boolean|true|none||none|
|»» channelList|[string]|true|none||none|
|»» bundleIdList|[string]|true|none||none|

## POST 根据openid获取用户崩溃详情

POST /uniform/openapi/getCrashUserInfo/platformId/platformId

根据openid获取用户崩溃详情

国内： https://crashsight.qq.com

新加坡： https://crashsight.wetest.net

以上示例中的前缀域名为示例域名，实际使用时以实际环境为准。

下载python代码示例：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getCrashUserInfo.py

> Body 请求参数

```json
{
  "requestid": "4f395abb53e82a1e1f57c7c86feb4cc4",
  "stime": "2021-12-26 00:00:00",
  "etime": "2021-12-27 00:00:00",
  "type": "pretty",
  "appId": "",
  "filters": {
    "user": [
      "597862998",
      "osewR0lNantT5rywYITNayOep-wA"
    ]
  },
  "limit": 10
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Content-Type|header|string| 否 ||none|
|Accept-Encoding|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» requestid|body|string| 否 ||请求id|
|» stime|body|string| 是 ||起始时间|
|» etime|body|string| 是 ||结束时间|
|» type|body|string| 否 ||返回格式|
|» appId|body|string| 否 ||项目列表|
|» filters|body|object| 是 ||筛选条件|
|»» user|body|[string]| 否 ||用户列表|
|» limit|body|integer| 否 ||返回条数|

> 返回示例

> 200 Response

```json
{
  "requestid": "string",
  "code": 0,
  "errmsg": "string",
  "data": {
    "columns": "string",
    "values": "string",
    "results": [
      {
        "issueId": "string",
        "crashTime": "string",
        "crashId": "string",
        "user": "string"
      }
    ]
  },
  "cost": 0
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» requestid|string|true|none||请求id|
|» code|integer|true|none||状态码|
|» errmsg|string|true|none||错误详情|
|» data|object|true|none||查询数据|
|»» columns|string|true|none||键值|
|»» values|string|true|none||值域|
|»» results|[object]|true|none||查询详情|
|»»» issueId|string|false|none||none|
|»»» crashTime|string|false|none||none|
|»»» crashId|string|false|none||none|
|»»» user|string|false|none||用户列表|
|» cost|integer|true|none||查询耗时|

# 数据模型

