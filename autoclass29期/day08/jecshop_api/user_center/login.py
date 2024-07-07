#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月24日
"""
import requests

# url = "http://newecshop.longtest.cn/shopapi/index.php/user/login?user=syz&passwd=123456"
# Response = requests.get(url=url, verify=False)

url = "http://newecshop.longtest.cn/shopapi/index.php/user/logi"
params = {
        'user': "syz",
        'passwd': 123456
}
Response = requests.get(url=url, params=params, verify=False)

info = [Response.text,
        Response.json(),
        Response.cookies,
        Response.headers,
        Response.request.headers,
        Response.elapsed,
        Response.url]
for i in info:
    print(i, end="\n")
