# # # # #  -*- coding:utf-8 -*-
# # # # """
# # # # 作者：张德宝
# 日期：2023年09月24日
# """
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
# # # #
# # # # url = "http://115.28.108.130/newecshop/admin/goods.php?is_ajax=1"
# # # # data_dict = {
# # # #     "act": "query",
# # # #     "cat_id": "",
# # # #     "intro_type": 0,
# # # #     "is_promote": 0,
# # # #     "stock_warning": 0,
# # # #     "brand_id": 0,
# # # #     "keyword": 16778087,
# # # #     "suppliers_id": "",
# # # #     "is_on_sale": "",
# # # #     "sort_by": "goods_id",
# # # #     "sort_order": "DESC",
# # # #     "extension_code": "",
# # # #     "is_delete": 0,
# # # #     "real_goods": 1,
# # # #     "supp": 0,
# # # #     "record_count": 1,
# # # #     "page_size": 15,
# # # #     "page": 1,
# # # #     "page_count": 1,
# # # #     "start": 0,
# # # #
# # # # }
# # # # print(data_dict)
# # # #
# # # # import json
# # # # json.dumps(data_dict)
# # # #
# # # # # c = {'sessionid': "ECSCP[last_choose]=2%7C; ECS_LastCheckOrder=Thu%2C%2010%20Apr%202025%2015%3A26%3A43%20GMT; ECSCP[lastfilterfile]=80EE692D; ECSCP[lastfilter]=a%253A19%253A%257Bs%253A6%253A%2522cat_id%2522%253Bi%253A0%253Bs%253A10%253A%2522intro_type%2522%253Bs%253A0%253A%2522%2522%253Bs%253A10%253A%2522is_promote%2522%253Bi%253A0%253Bs%253A13%253A%2522stock_warning%2522%253Bi%253A0%253Bs%253A8%253A%2522brand_id%2522%253Bi%253A0%253Bs%253A7%253A%2522keyword%2522%253Bs%253A8%253A%252216778087%2522%253Bs%253A12%253A%2522suppliers_id%2522%253Bs%253A0%253A%2522%2522%253Bs%253A10%253A%2522is_on_sale%2522%253Bs%253A0%253A%2522%2522%253Bs%253A7%253A%2522sort_by%2522%253Bs%253A8%253A%2522goods_id%2522%253Bs%253A10%253A%2522sort_order%2522%253Bs%253A4%253A%2522DESC%2522%253Bs%253A14%253A%2522extension_code%2522%253Bs%253A0%253A%2522%2522%253Bs%253A9%253A%2522is_delete%2522%253Bi%253A0%253Bs%253A10%253A%2522real_goods%2522%253Bi%253A1%253Bs%253A4%253A%2522supp%2522%253Bi%253A0%253Bs%253A12%253A%2522record_count%2522%253Bs%253A1%253A%25221%2522%253Bs%253A9%253A%2522page_size%2522%253Bi%253A15%253Bs%253A4%253A%2522page%2522%253Bi%253A1%253Bs%253A10%253A%2522page_count%2522%253Bd%253A1%253Bs%253A5%253A%2522start%2522%253Bi%253A0%253B%257D; ECSCP[lastfiltersql]=U0VMRUNUIGdvb2RzX2lkLCBnb29kc19uYW1lLCBnb29kc190eXBlLCBnb29kc19zbiwgc2hvcF9wcmljZSwgaXNfb25fc2FsZSwgaXNfYmVzdCwgaXNfbmV3LCBpc19ob3QsIHNvcnRfb3JkZXIsIGdvb2RzX251bWJlcixleGNsdXNpdmUsIGludGVncmFsLCAgKHByb21vdGVfcHJpY2UgPiAwIEFORCBwcm9tb3RlX3N0YXJ0X2RhdGUgPD0gJzE3NDQyNzAwMTknIEFORCBwcm9tb3RlX2VuZF9kYXRlID49ICcxNzQ0MjcwMDE5JykgQVMgaXNfcHJvbW90ZSAsIHN1cHBsaWVyX3N0YXR1cywgc3VwcGxpZXJfaWQgIEZST00gYG5ld2Vjc2hvcGAuYGVjc19nb29kc2AgQVMgZyBXSEVSRSBpc19kZWxldGU9JzAnICBBTkQgKGdvb2RzX3NuIExJS0UgJyUxNjc3ODA4NyUnIE9SIGdvb2RzX25hbWUgTElLRSAnJTE2Nzc4MDg3JScpIEFORCBpc19yZWFsPScxJ0FORCBnLnN1cHBsaWVyX2lkID0gMCBPUkRFUiBCWSBnb29kc19pZCBERVNDICBMSU1JVCAwLDE1; ecshop_affiliate_uid=16564; ECS[history]=91; PHPSESSID=d17v6kapas4gq58abh1b96jbm1; one_step_buy=1; real_ipd=223.104.41.254; ECS_ID=af3707d76684a16e210a9ab469b7a0006d2da2ee; ECSCP_ID=41112ee366ac3a1414379a160b5c81a29f790480"
# # # # # }
# # # # headers = {'cookie':'ECSCP[last_choose]=2%7C; ECS_LastCheckOrder=Thu%2C%2010%20Apr%202025%2015%3A26%3A43%20GMT; ECSCP[lastfilterfile]=80EE692D; ECSCP[lastfilter]=a%253A19%253A%257Bs%253A6%253A%2522cat_id%2522%253Bi%253A0%253Bs%253A10%253A%2522intro_type%2522%253Bs%253A0%253A%2522%2522%253Bs%253A10%253A%2522is_promote%2522%253Bi%253A0%253Bs%253A13%253A%2522stock_warning%2522%253Bi%253A0%253Bs%253A8%253A%2522brand_id%2522%253Bi%253A0%253Bs%253A7%253A%2522keyword%2522%253Bs%253A8%253A%252216778087%2522%253Bs%253A12%253A%2522suppliers_id%2522%253Bs%253A0%253A%2522%2522%253Bs%253A10%253A%2522is_on_sale%2522%253Bs%253A0%253A%2522%2522%253Bs%253A7%253A%2522sort_by%2522%253Bs%253A8%253A%2522goods_id%2522%253Bs%253A10%253A%2522sort_order%2522%253Bs%253A4%253A%2522DESC%2522%253Bs%253A14%253A%2522extension_code%2522%253Bs%253A0%253A%2522%2522%253Bs%253A9%253A%2522is_delete%2522%253Bi%253A0%253Bs%253A10%253A%2522real_goods%2522%253Bi%253A1%253Bs%253A4%253A%2522supp%2522%253Bi%253A0%253Bs%253A12%253A%2522record_count%2522%253Bs%253A1%253A%25221%2522%253Bs%253A9%253A%2522page_size%2522%253Bi%253A15%253Bs%253A4%253A%2522page%2522%253Bi%253A1%253Bs%253A10%253A%2522page_count%2522%253Bd%253A1%253Bs%253A5%253A%2522start%2522%253Bi%253A0%253B%257D; ECSCP[lastfiltersql]=U0VMRUNUIGdvb2RzX2lkLCBnb29kc19uYW1lLCBnb29kc190eXBlLCBnb29kc19zbiwgc2hvcF9wcmljZSwgaXNfb25fc2FsZSwgaXNfYmVzdCwgaXNfbmV3LCBpc19ob3QsIHNvcnRfb3JkZXIsIGdvb2RzX251bWJlcixleGNsdXNpdmUsIGludGVncmFsLCAgKHByb21vdGVfcHJpY2UgPiAwIEFORCBwcm9tb3RlX3N0YXJ0X2RhdGUgPD0gJzE3NDQyNzAwMTknIEFORCBwcm9tb3RlX2VuZF9kYXRlID49ICcxNzQ0MjcwMDE5JykgQVMgaXNfcHJvbW90ZSAsIHN1cHBsaWVyX3N0YXR1cywgc3VwcGxpZXJfaWQgIEZST00gYG5ld2Vjc2hvcGAuYGVjc19nb29kc2AgQVMgZyBXSEVSRSBpc19kZWxldGU9JzAnICBBTkQgKGdvb2RzX3NuIExJS0UgJyUxNjc3ODA4NyUnIE9SIGdvb2RzX25hbWUgTElLRSAnJTE2Nzc4MDg3JScpIEFORCBpc19yZWFsPScxJ0FORCBnLnN1cHBsaWVyX2lkID0gMCBPUkRFUiBCWSBnb29kc19pZCBERVNDICBMSU1JVCAwLDE1; ecshop_affiliate_uid=16564; ECS[history]=91; PHPSESSID=d17v6kapas4gq58abh1b96jbm1; one_step_buy=1; real_ipd=223.104.41.254; ECS_ID=af3707d76684a16e210a9ab469b7a0006d2da2ee; ECSCP_ID=41112ee366ac3a1414379a160b5c81a29f790480',
# # # #     'Content-Type': 'application/x-www-form-urlencoded', "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.9",
# # # #            "Connection": "keep-alive",  "Origin": "http://115.28.108.130",  "Referer": "http://115.28.108.130/newecshop/admin/goods.php?act=list",
# # # #            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}
# # # # Response = requests.post(url=url, data=data_dict, headers=headers)
# # # # print(Response.text)
# # # #
# # # # # 断言状态码为200
# # # # assert Response.status_code == 200, f"请求失败，状态码为: {Response.status_code}"
# # # # # 断言响应内容中包含错误信息"error":1
# # # # assert '"error":1' in Response.text
# # # # # 断言响应内容不为空
# # # # assert Response.text != "", "响应内容为空"
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # url = 'http://115.28.108.130/newecshop/admin/privilege.php'
# # #
# # # data = {
# # #     "username": "admin",
# # #     "password": "admin123",
# # #     "act": "signin"}
# # #
# # # Response = requests.post(url=url, data=data)
# # #
# # # print(Response.text)
# # #
# # #
# # #
# # #
# # # s1 = '\'hello, world!\''
# # # s2 = '\\hello, world!\\'
# # # print(s1)
# # # print(s2)
# # #
# # # s1 = '\it \is \time \to \read \now'
# # # s2 = r'\it \is \time \to \read \now'
# # # print(s1)
# # # print(s2)
# # #
# # #
# # #
# #
# #
# # # import requests
# # # url = 'https://httpbin.org/post'
# # # data = {'name': '临渊', 'password': '123456'}
# # # res = requests.post(url, data=data, verify=False)
# # # print(res.text)
# # #
# # # res_dict = res.json()
# # # assert 'https://httpbin.org/post' == res_dict.get(url)
# #
# #
# #
# # import requests
# #
# # url = 'http://115.28.108.130/newecshop/admin/users.php'
# #
# # data = {
# #     'email': "1282038045@qq.com",
# #     'username': "zhangdebao222",
# #     'password': "123456",
# #     'confirm_password':	"123456",
# #     'mobile_phone': '15200001113'
# # }
# #
# # headers = {
# #     "Host": "115.28.108.130",
# #     "Cache-Control": "max-age=0",
# #     "Upgrade-Insecure-Requests": "1",
# #     "Origin": "http://115.28.108.130",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
# #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
# #     "Referer": "http://115.28.108.130/newecshop/admin/users.php?act=add",
# #     "Accept-Language": "zh-CN,zh;q=0.9",
# #     "Cookie": "ECSCP[lastfilterfile]=1483A5E9; ECSCP[lastfilter]=a%253A11%253A%257Bs%253A8%253A%2522keywords%2522%253Bs%253A0%253A%2522%2522%253Bs%253A4%253A%2522rank%2522%253Bi%253A0%253Bs%253A13%253A%2522pay_points_gt%2522%253Bi%253A0%253Bs%253A13%253A%2522pay_points_lt%2522%253Bi%253A0%253Bs%253A7%253A%2522sort_by%2522%253Bs%253A7%253A%2522user_id%2522%253Bs%253A10%253A%2522sort_order%2522%253Bs%253A4%253A%2522DESC%2522%253Bs%253A12%253A%2522record_count%2522%253Bs%253A5%253A%252216419%2522%253Bs%253A9%253A%2522page_size%2522%253Bi%253A15%253Bs%253A4%253A%2522page%2522%253Bi%253A1%253Bs%253A10%253A%2522page_count%2522%253Bd%253A1095%253Bs%253A5%253A%2522start%2522%253Bi%253A0%253B%257D; ECSCP[lastfiltersql]=U0VMRUNUIHVzZXJfaWQsIHVzZXJfbmFtZSwgZW1haWwsIG1vYmlsZV9waG9uZSwgaXNfdmFsaWRhdGVkLCB2YWxpZGF0ZWQsIHVzZXJfbW9uZXksIGZyb3plbl9tb25leSwgcmFua19wb2ludHMsIHBheV9wb2ludHMsIHN0YXR1cywgcmVnX3RpbWUsIGZyb21zICBGUk9NIGBuZXdlY3Nob3BgLmBlY3NfdXNlcnNgIFdIRVJFIDEgIE9SREVSIGJ5IHVzZXJfaWQgREVTQyBMSU1JVCAwLDE1; ECS_LastCheckOrder=Thu%2C%2017%20Apr%202025%2016%3A17%3A02%20GMT; ECS[history]=91; PHPSESSID=d17v6kapas4gq58abh1b96jbm1; one_step_buy=1; real_ipd=114.246.237.215; ECSCP_ID=bd642b8dddf991d9ca78ad371344c90b826d195f; ECS_ID=6ee58b19d90ebe9be189331c37bc939ec5d56081",
# #     "Postman-Token": "ccd310a8-8cce-42c9-9733-be5f9d8ac609",
# #     "Accept-Encoding": "gzip, deflate, br",
# #     "Content-Type": "multipart/form-data; boundary=--------------------------533984641215415722943074",
# #     "Content-Length": "2610",
# #     "Connection": "keep-alive"
# # }
# # Response = requests.post(url=url, data=data, headers=headers)
# # print(Response.text)
# # -------------------------------------------------------------------------------------------------------------------------------
#
#
# # Ecshop 后台注册会员号接口
# # import requests
# #
# # url = 'http://115.28.108.130/newecshop/admin/users.php'
# #
# # data = {
# #     'email': "1282038045@qq.com",
# #     'username': "zhangdebao222",
# #     'password': "123456",
# #     'confirm_password': "123456",
# #     'mobile_phone': '15200001113',
# #     'act': 'insert'
# # }
# #
# # headers = { "Origin": "http://115.28.108.130", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# # AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
# #
# # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,
# # application/signed-exchange;v=b3;q=0.7",
# #
# # "Referer": "http://115.28.108.130/newecshop/admin/users.php?act=add", "Accept-Language": "zh-CN,zh;q=0.9",
# # "Cookie": "ECSCP[lastfilterfile]=1483A5E9; ECSCP[
# # lastfilter]=a%253A11%253A%257Bs%253A8%253A%2522keywords%2522%253Bs%253A0%253A%2522%2522%253Bs%253A4%253A%2522rank
# # %2522%253Bi%253A0%253Bs%253A13%253A%2522pay_points_gt%2522%253Bi%253A0%253Bs%253A13%253A%2522pay_points_lt%2522
# # %253Bi%253A0%253Bs%253A7%253A%2522sort_by%2522%253Bs%253A7%253A%2522user_id%2522%253Bs%253A10%253A%2522sort_order
# # %2522%253Bs%253A4%253A%2522DESC%2522%253Bs%253A12%253A%2522record_count%2522%253Bs%253A5%253A%252216419%2522%253Bs
# # %253A9%253A%2522page_size%2522%253Bi%253A15%253Bs%253A4%253A%2522page%2522%253Bi%253A1%253Bs%253A10%253A
# # %2522page_count%2522%253Bd%253A1095%253Bs%253A5%253A%2522start%2522%253Bi%253A0%253B%257D; ECSCP[ lastfiltersql
# # ]=U0VMRUNUIHVzZXJfaWQsIHVzZXJfbmFtZSwgZW1haWwsIG1vYmlsZV9waG9uZSwgaXNfdmFsaWRhdGVkLCB2YWxpZGF0ZWQsIHVzZXJfbW9uZXksIGZyb3plbl9tb25leSwgcmFua19wb2ludHMsIHBheV9wb2ludHMsIHN0YXR1cywgcmVnX3RpbWUsIGZyb21zICBGUk9NIGBuZXdlY3Nob3BgLmBlY3NfdXNlcnNgIFdIRVJFIDEgIE9SREVSIGJ5IHVzZXJfaWQgREVTQyBMSU1JVCAwLDE1; ECS_LastCheckOrder=Thu%2C%2017%20Apr%202025%2016%3A17%3A02%20GMT; ECS[history]=91; PHPSESSID=d17v6kapas4gq58abh1b96jbm1; one_step_buy=1; real_ipd=114.246.237.215; ECSCP_ID=bd642b8dddf991d9ca78ad371344c90b826d195f; ECS_ID=6ee58b19d90ebe9be189331c37bc939ec5d56081", "Connection": "keep-alive" }
# #
# # try:
# #     # 使用 files 参数处理 multipart/form-data 格式
# #     response = requests.post(url=url, data=data, headers=headers)
# #     response.raise_for_status()  # 检查请求是否成功
# #     print(response.text)
# # except requests.exceptions.HTTPError as http_err:
# #     print(f'HTTP error occurred: {http_err}')
# # except requests.exceptions.RequestException as req_err:
# #     print(f'Request error occurred: {req_err}')
#
#
# # -------------------------------------------------------------------------------------------------------------------------------
# # Python中常用的占位符有：
# print('%s' % {'a': 1, 'b': 2})
# print('%10s' % 'hello')
# print('%d' % 3.0)
# print('%.2f' % 1.999)
# print('%x' % 16)