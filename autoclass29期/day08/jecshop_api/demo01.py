#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月24日
"""
import json
import requests

url = 'https://httpbin.org/post'

d = {
        "keyword": "奶粉",
        "type": "search",
        "page":	1,
        "order": 0,
        "filtrate": ""
}
d = json.dumps(d)
c = {
    'sessionid': "123456"
}
headers = {'Content-Type': 'application/json'}
Response = requests.post(url=url, headers=headers, cookies=c, json=d)

info = [Response.text,
        Response.json(),
        Response.status_code,
        Response.cookies,
        Response.headers,
        Response.request.headers,
        Response.elapsed,
        Response.url]
for i in info:
    print(i, end="\n")