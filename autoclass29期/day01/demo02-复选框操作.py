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


checkboxs = mydriver.find_elements(by=By.CLASS_NAME, value="form-check-input")

for i in range(199):
    for i in checkboxs:
        sleep(0.01)
        i.click()