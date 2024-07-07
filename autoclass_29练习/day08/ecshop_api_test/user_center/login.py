#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年12月02日
"""
import requests

url = "http://newecshop.longtest.cn/shopapi/index.php/user/login"

parmas = {
    'user': "syz",
    'passwd': "123456"
}
Response = requests.get(url=url, params=parmas, verify=False)

info = [
    Response.text,
    Response.json,
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
