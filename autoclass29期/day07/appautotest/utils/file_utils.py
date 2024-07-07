#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月17日
"""
from appium import webdriver
class FileUtils:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def push_file(self, source, des):
        self.driver.push_file(source_path=source, destination_path=des)