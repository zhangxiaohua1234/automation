#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def openTestPage():
    myoptions = ChromeOptions()
    myoptions.add_experimental_option("detach", True)
    mydriver = webdriver.Chrome(options=myoptions)
    mydriver.implicitly_wait(5)
    mydriver.get(r"D:\python_files\autoclass29期\selenium_demo\selenium_demo\selenium.html")

    return mydriver