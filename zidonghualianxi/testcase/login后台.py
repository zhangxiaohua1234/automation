#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2025年05月11日
"""
# ---------------------------------------------------------------------------------商城后台-登录
import requests
# class TestApi:
#     # 类变量
#     cookie = ""

    # def testlogin(self):
    #     # 商城后台-登录
    #     url = 'http://115.28.108.130/newecshop/admin/privilege.php'
    #
    #     url_params = {
    #         "username": "admin",
    #         "password": "admin123",
    #         "act": "signin",
    #     }
    #
    #     headers = {
    #         "Host": "115.28.108.130",
    #         "Cache-Control": "max-age=0",
    #         "Upgrade-Insecure-Requests": "1",
    #         "Origin": "http://115.28.108.130",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                       "Chrome/125.0.0.0 Safari/537.36",
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
    #                   "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #         "Referer": "http://115.28.108.130/newecshop/admin/privilege.php?act=logout",
    #         "Accept-Language": "zh-CN,zh;q=0.9",
    #         "Cookie": "ECS_LastCheckOrder=Thu%2C%2008%20May%202025%2016%3A46%3A43%20GMT; ECS[history]=91; "
    #                   "real_ipd=221.216.116.249; ECS_ID=27901d0b00d2b67610846e88fe03f054d5fe866d; "
    #                   "ECSCP_ID=32e61650264cc822e8e9e7b9c2014f79e826c046",
    #         "Postman-Token": "776c13f4-ebe5-427c-8da4-f3632046a04e",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Content-Type": "application/x-www-form-urlencoded",
    #         "Content-Length": "43",
    #         "Connection": "keep-alive"
    #     }
    #     res = requests.post(url, data=url_params, headers=headers, verify=False)
    #
    #     info = [
    #         res.text,
    #         res.url,
    #         res.headers,
    #         res.cookies,
    #         res.request.headers
    #     ]
    #     for i in info:
    #         print(i, end='\n')
    #
    #     result = res.request.headers
    #     TestApi.cookie = result.get("Cookie")
    #     print("打印cookie %s" % TestApi.cookie)

    # def testliebiao(self):
    #     # 商城后台-管理中心商品列表(注意cookie 过期)
    #     url = 'http://115.28.108.130/newecshop/admin/goods.php?act=ajax_category'
    #
    #     headers = {
    #         "Host": "115.28.108.130",
    #         "Accept": "text/plain, */*; q=0.01",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                       "Chrome/125.0.0.0 Safari/537.36",
    #         "X-Requested-With": "XMLHttpRequest",
    #         "Referer": "http://115.28.108.130/newecshop/admin/goods.php?act=list",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Accept-Language": "zh-CN,zh;q=0.9",
    #         "Cookie": "ECS_LastCheckOrder=Thu%2C%2008%20May%202025%2016%3A46%3A43%20GMT; ECS[history]=91; "
    #                   "real_ipd=221.216.116.249; ECS_ID=27901d0b00d2b67610846e88fe03f054d5fe866d; "
    #                   "ECSCP_ID=32e61650264cc822e8e9e7b9c2014f79e826c046",
    #         "If-Modified-Since": "Thu, 08 May 2025 17:26:58 GMT",
    #         "Connection": "keep-alive"
    #     }
    #     res = requests.post(url, headers=headers, verify=False)
    #
    #     info = [
    #         res.json(),
    #         res.url,
    #         res.headers,
    #         res.cookies
    #     ]
    #     for i in info:
    #         print(i, end='\n')


# if __name__ == '__main__':
#     TestApi().testlogin()

# 商城后台登录与列表查询进行接口关联 不太好关联；登录cookie是：real_ipd=114.246.239.44; ECSCP_ID=57a59018c83c5427f1455f4ac2c2e5664b58462e；
# 列表
# 查询的cookie是一长串：ECS_LastCheckOrder=Thu%2C%2008%20May%202025%2016%3A46%3A43%20GMT;
# ECS[history]=91; real_ipd=221.216.116.249;
# ECS_ID=27901d0b00d2b67610846e88fe03f054d5fe866d; ECSCP_ID=32e61650264cc822e8e9e7b9c2014f79e826c046
# 如果把登录的TestApi.cookie 放到列表查询的headers中cookie里边去，返回的是前端代码。整明还是cookie不对。
# 以下是测试登录发送的实际cookie 和 列表发送请求时实际的cookie

# ------------------------------------------------------------------------------登录接口
# import requests
# class TestApi:
#     cookie = ""


# url = 'http://115.28.108.130/newecshop/admin/privilege.php'
# url_params = {
#     "username": "admin",
#     "password": "admin123",
#     "act": "signin",
# }
#
# headers = { "Host": "115.28.108.130", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (
# KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded",
# "Cookie": "ECS_LastCheckOrder=Thu, 08 May 2025 16:46:43 GMT; ECS[history]=91; real_ipd=221.216.116.249;
# ECS_ID=27901d0b00d2b67610846e88fe03f054d5fe866d; ECSCP_ID=32e61650264cc822e8e9e7b9c2014f79e826c046" }
#
# res = requests.post(url, data=url_params, headers=headers, verify=False)
#
# # 打印实际发送的 Cookie
# sent_cookie = res.request.headers.get("Cookie")
# print("实际发送的 Cookie:", sent_cookie)
#
# # 保存到 TestApi.cookie
# TestApi.cookie = sent_cookie
# print("存储的完整 Cookie:", TestApi.cookie)

# ------------------------------------------------------------------------------列表接口
# import requests
#
# class TestApi:
#     cookie = ""
#
# url = 'http://115.28.108.130/newecshop/admin/goods.php?act=ajax_category'
#
# headers = { "Host": "115.28.108.130", "Accept": "text/plain, */*; q=0.01", "User-Agent": "Mozilla/5.0 (Windows NT
# 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 " "Safari/537.36", "X-Requested-With":
# "XMLHttpRequest", "Referer": "http://115.28.108.130/newecshop/admin/goods.php?act=list", "Accept-Encoding": "gzip,
# deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie":
# "ECS_LastCheckOrder=Thu%2C%2008%20May%202025%2016%3A46%3A43%20GMT; ECS[history]=91; real_ipd=221.216.116.249;
# ECS_ID=27901d0b00d2b67610846e88fe03f054d5fe866d; ECSCP_ID=32e61650264cc822e8e9e7b9c2014f79e826c046",
# "If-Modified-Since": "Thu, 08 May 2025 17:26:58 GMT", "Connection": "keep-alive" } res = requests.post(url,
# headers=headers, verify=False)
#
# # 打印实际发送的 Cookie
# sent_cookie = res.request.headers.get("Cookie")
# print("实际发送的 Cookie:", sent_cookie)
#
# # 保存到 TestApi.cookie
# TestApi.cookie = sent_cookie
# print("存储的完整 Cookie:", TestApi.cookie)
