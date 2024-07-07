#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月17日
"""
from conftest import webdriver

module = {
    "1":"main_bottom_home",
    "2":"main_bottom_category",
    "3":"main_bottom_discovery",
    "4":"main_bottom_",
}


class SelectPage:
    def __init__(self, dervier:webdriver.Remote):
        self.derver = dervier


    def goto_module(page):
        pass
