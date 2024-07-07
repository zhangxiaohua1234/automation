#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年06月12日
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


def openTestPage():
    myoptions = ChromeOptions()
    myoptions.add_experimental_option("detach", True)
    mydriver = webdriver.Chrome(options=myoptions)
    mydriver.implicitly_wait(10)
    mydriver.get(r'D:\python_files\pythonProject10\pythonclasses\autoclass29\selenium_demo\selenium_demo\selenium.html')
    return mydriver
