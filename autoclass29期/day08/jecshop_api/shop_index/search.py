#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月24日
"""
import requests


url = "https://newecshop.longtest.cn/shopapi/index.php/first/index"
d = {
        "keyword": "奶粉",
        "type": "search",
        "page":	1,
        "order": 0,
        "filtrate": ""
}

import json
json.dumps(d)
print(d)

Response = requests.post(url=url, data=d, verify=False)

info = [Response.text,
        Response.json,
        Response.status_code,
        Response.cookies,
        Response.headers,
        Response.request.headers,
        Response.elapsed,
        Response.url]
for i in info:
    print(i, end="\n")