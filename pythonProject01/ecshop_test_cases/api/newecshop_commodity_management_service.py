#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年05月31日
"""
import requests


class product_search:
    path = "/newecshop/admin/goods.php?is_ajax=1"

    def send(self, url="", method="get", header="", data=""):
        return requests.request(url=url, method=method, headers=header, data=data)


class products_add:
    pstats = "/newecshop/admin/goods.php?act=add"

    def send(self, url="", method="get", header="", data=""):
        return requests.request(url=url, method=method, headers=header, data=data)
