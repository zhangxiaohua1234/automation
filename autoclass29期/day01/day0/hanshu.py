#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月18日
"""

from selenium.webdriver.common.by import By


class options():
    def __init__(self, wd):
        self.wd = wd

    def id(self, ids):
        return self.wd.find_element(By.ID, value=ids)

    def classa(self, cls):
        return self.wd.find_element(By.CLASS_NAME, value=cls)

    def xpath(self, xps):
        return self.wd.find_element(By.XPATH, value=xps)

    def name(self, names):
        return self.wd.find_element(By.NAME, value=names)
