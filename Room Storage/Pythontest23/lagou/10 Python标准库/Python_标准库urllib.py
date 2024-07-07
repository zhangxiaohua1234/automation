#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年06月11日
"""
"""
urllib 库
python 2
import urllib2
response=urllib2.urlopen("http://www.baidu.com")
python 3
import urllib.request
response=urllib.request.urlopen('http://www.baidu.com')
"""
import urllib.request

response: object = urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print(response.read())
print(response.headers)
