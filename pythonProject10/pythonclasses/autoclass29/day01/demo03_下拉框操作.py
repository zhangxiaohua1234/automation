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
xpath = '//*[@id="area"]/option[2]'
selector = chromeDriver.find_element(by=By.XPATH, value=xpath)
selector.click()


input()
