#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2025年05月11日
"""
import requests


class RequestUtils:
    sess = requests.session()

    def send_all_request(self, **kwargs):
        res = RequestUtils.sess.request(**kwargs)
        print("响应的值：%s" % res.json())
        return res