#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月17日
"""
from appium import webdriver


class DvicesInfo:
    def __init__(self, driver:webdriver.Rmotate):
        self.driver = driver
        self.driver_info = {}