#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2025年05月08日
"""
import jsonpath
import requests
# ---------------------------------------------------------------------------------商城前台-登录
# 前台返回的都是html代码，故没办法练习接口测试

# url = 'http://115.28.108.130/newecshop/user.php?act=act_login'
# url_params = {
#     "username": "zdb123",
#     "password": "123456",
#     "captcha": "undefined",
#     "back_act": "http://115.28.108.130/newecshop/search.php?encode=YTozOntzOjQ6InR5cGUiO3M6MToiMCI7czo4OiJrZXl3b3JkcyI7czozOiIyMjIiO3M6MTg6InNlYXJjaF9lbmNvZGVfdGltZSI7aToxNzQ0Mjk4MjE4O30 = "}
#
# headers = {
#     "Host": "115.28.108.130",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Accept": "*/*",
#     "Origin": "http://115.28.108.130",
#     "Referer": "http://115.28.108.130/newecshop/user.php",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Cookie": "ECS[history]=91; real_ipd=221.216.116.249; ECS_ID=27901d0b00d2b67610846e88fe03f054d5fe866d; ECSCP_ID=32e61650264cc822e8e9e7b9c2014f79e826c046"
# }
# res = requests.post(url, data=url_params, headers=headers)
# try:
#     res_dict = res.json()
#     print('响应文本转为字典', res_dict)
#     print('提取响应数据args', res_dict.get('args'))
# except:
#     print('响应文本', res.text)
