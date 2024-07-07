#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月27日
"""
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver: Chrome):
        self.mydriver = driver

    def find_element(self, by, value):
        return WebDriverWait(self.mydriver, 30, 1).until(
            EC.visibility_of_element_located((by, value))
        )