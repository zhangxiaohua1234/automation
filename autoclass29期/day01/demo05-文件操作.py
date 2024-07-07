#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月06日
"""

from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

# from webdriver_manager.chrome import webdriver

mydriver = webdriver.Chrome()


mydriver.get(r"D:\autoclass29期\selenium_demo\selenium_demo\selenium.html")


file_btn = mydriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div[1]/input")

file_btn.send_keys(r"D:\autoclass29期\day01\demo00-selenium基础-八大元素定位方法.py")

