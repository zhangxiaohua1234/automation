#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年12月03日
"""

import requests
import json

url = "https://httpbin.org/post"

data = {
    'order': 0,
    'filtrate': "",
    'keyword': "奶粉",
    'type': "search",
    'page': 1
}

d = json.dumps(data)
c = {
    "sessionid": '123456',
    "token": 'asdf'
}
headers = {
    'Content-Type': 'application/json',
    'cookies': 'sessionid=123,token=adfsa'
}
Response = requests.post(url=url, json=data, cookies=c, headers=headers)

info = [
    Response.text,
    Response.json(),
    # Response.status_code,
    # Response.headers,
    # Response.url,
    # Response.request.method,
    # Response.request.url,
    # Response.request.body,
    Response.request.headers
]

for i in info:
    print(i, end='\n')