#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2025年05月11日
"""
# ---------------------------------------------------------------------------------商城后台-登录
import requests

from zidonghualianxi练习.commons.request_utils import RequestUtils


class TestApi:
    # 类变量
    cookie = ""

    def test_a(self):
        # 商城后台-管理中心商品列表(注意cookie 过期)
        method = "get"
        url = 'http://115.28.108.130/newecshop/admin/goods.php?act=ajax_category'

        headers = {
            "Host": "115.28.108.130",
            "Accept": "text/plain, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/125.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://115.28.108.130/newecshop/admin/goods.php?act=list",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "ECS_LastCheckOrder=Sun%2C%2011%20May%202025%2011%3A04%3A40%20GMT; ECS[display]=grid; ECS["
                      "history]=78%2C91; ECSCP_ID=fa8ef4c207a075e1e4da6abe98489c106e75acef; "
                      "ECS_ID=dfcee76e1de8d4da994ad9cdaee02d7a2226fbca; real_ipd=114.246.239.44",
            "If-Modified-Since": "Thu, 08 May 2025 17:26:58 GMT",
            "Connection": "keep-alive"
        }
        res = RequestUtils().send_all_request(method=method, url=url, headers=headers, verify=False)

    def test_b(self):
        # 商城后台-管理中心商品列表(注意cookie 过期)
        method = "get"
        url = 'http://115.28.108.130/newecshop/admin/goods.php?act=ajax_category'

        headers = {
            "Host": "115.28.108.130",
            "Accept": "text/plain, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/125.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://115.28.108.130/newecshop/admin/goods.php?act=list",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "ECS_LastCheckOrder=Sun%2C%2011%20May%202025%2011%3A04%3A40%20GMT; ECS[display]=grid; ECS["
                      "history]=78%2C91; ECSCP_ID=fa8ef4c207a075e1e4da6abe98489c106e75acef; "
                      "ECS_ID=dfcee76e1de8d4da994ad9cdaee02d7a2226fbca; real_ipd=114.246.239.44",
            "If-Modified-Since": "Thu, 08 May 2025 17:26:58 GMT",
            "Connection": "keep-alive"
        }
        res = RequestUtils().send_all_request(method=method, url=url, headers=headers, verify=False)


if __name__ == '__main__':
    TestApi().testlogin_a()
