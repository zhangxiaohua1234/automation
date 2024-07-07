#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年12月02日
"""
import requests

import json

url = "http://newecshop.longtest.cn/shopapi/index.php/first/index"

data = {
    'order': 0,
    'filtrate': "",
    'keyword': "奶粉",
    'type': "search",
    'page': 1
}
# d = json.dumps(data)
# print(d)


Response = requests.post(url=url, data=data, verify=False)

info = [
    Response.text,
    Response.json(),
    Response.status_code,
    Response.headers,
    Response.elapsed,
    Response.url,
    Response.request.headers,
    Response.request.body,
    Response.request.method
]

for i in info:
    print(i, end='\n')