#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年06月06日
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chromeDriver = webdriver.Chrome()

chromeDriver.get(r"D:\python_files\pythonProject10\pythonclasses\autoclass29\selenium_demo\selenium_demo\selenium.html")

checkboxs = chromeDriver.find_elements(by=By.CLASS_NAME, value="form-check-input")
for i in range(20):
    for i in checkboxs:
        sleep(0.1)
        i.click()

input()
