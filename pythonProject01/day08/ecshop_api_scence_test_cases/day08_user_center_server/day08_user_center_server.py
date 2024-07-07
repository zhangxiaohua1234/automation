#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年05月10日
"""
import requests
import json

# 商城前台--登录 没有调试通过
# url = "http://115.28.108.130/newecshop/user.php?act=act_login"
#
# params = {
#     "username": "zdb123",
#     "password": 123456,
#     "captcha": "undefined",
#     "back_act": "http://115.28.108.130/newecshop/index.php"
# }
#
# header = {
#     "Host": "115.28.108.130",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Accept": "*/*",
#     "Origin": "http://115.28.108.130",
#     "Referer": "http://115.28.108.130/newecshop/user.php",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "keep-alive"
# }
#
# cookie = {
#     "ecshop_affiliate_uid": "16564",
#     "real_ipd": "120.245.63.169",
#     "ECSCP_ID": "b64ce43a27aeb1d70f0886fc7630fd10fd069ebd",
#     "ECS_ID": "14a2cf2aa3583b6e09899b60bc3e32b63a81abc4"
# }
# Response = requests.get(url=url, params=params, headers=header, cookies=cookie, verify=False)
# print(Response.text)


# # 上陈后台--商品搜索

# url = "http://115.28.108.130/newecshop/admin/goods.php?is_ajax=1"
#
# data = {
#     "act": "query",
#     "cat_id": "",
#     "intro_type": "0",
#     "is_promote": "0",
#     "stock_warning": "0",
#     "brand_id": "0",
#     "keyword": "uuuu",
#     "suppliers_id": "",
#     "is_on_sale": "",
#     "sort_by": "goods_id",
#     "sort_order": "DESC",
#     "extension_code": "",
#     "is_delete": "0",
#     "real_goods": "1",
#     "supp": "0",
#     "record_count": "1",
#     "page_size": "15",
#     "page": "1",
#     "page_count": "1",
#     "start": "0"
# }
# 将data转换成json格式 带有”“
# data1 = json.dumps(data)
# print(data1)
# header = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Content-Length": "",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Connection": "keep-alive",
#     "Host": "115.28.108.130",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 "
#                   "Safari/537.36",
#     "Accept": "*/*",
#     "Origin": "http://115.28.108.130",
#     "Referer": "http://115.28.108.130/newecshop/admin/goods.php?act=list",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
# }
# cookie = {
#     "ECSCP_ID": "b64ce43a27aeb1d70f0886fc7630fd10fd069ebd",
#     "ECS_ID": "14a2cf2aa3583b6e09899b60bc3e32b63a81abc4"}
# Response = requests.post(url=url, data=data, headers=header, cookies=cookie, verify=False)
#
# info = [
#     Response.text,
#     Response.json,
#     Response.status_code,
#     Response.headers,
#     Response.elapsed,
#     Response.url,
#     Response.request.headers,
#     Response.request.body,
#     Response.request.method
# ]
#
# for i in info:
#     print(i, end="\n")
#
# print(info)

# url = 'https://httpbin.org/post'
# data = {'name': '临渊', 'password': '123456'}
# res = requests.post(url, data=data)
# print(res.text)
#
# res_dict = res.json()
# form = res_dict.get('form')
# assert "https://httpbin.org/post" == res_dict.get('url')
# assert form and "临渊" == form.get('name') and '123456' == form.get('password')


# url = 'https://httpbin.org/post'
# json_data = {'name': '临渊', 'age': 18, 'on_site': True, 'favorite': None}
# res = requests.post(url, json=json_data)
# print(res.text)


# url = 'https://httpbin.org/get'
# url_params = {'name': '临渊', 'age': '18'}
# res = requests.get(url, params=url_params)
# print(res.text)
# try:
#     res_dict = res.json()
#     print('响应文本转为字典', res_dict)
#     print('提取响应数据args', res_dict.get('args'))
# except:
#     print('响应文本', res.text)


login_url = "http://115.28.108.130/newecshop/user.php?act=act_login"
data = {
    "username": "zdb123",
    "password": 123456,
    "captcha": "undefined",
    "back_act": "http://115.28.108.130/newecshop/index.php/user/login"
}
headers = {

    "Host": "115.28.108.130",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Origin": "http://115.28.108.130",
    "Referer": "http://115.28.108.130/newecshop/user.php",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Postman-Token": "90446431-b069-42fa-8dd1-f394d0b753e9",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
}

Response = requests.post(url=login_url, data=data, verify=False)

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
    print(i, end="\n")

print(info)
