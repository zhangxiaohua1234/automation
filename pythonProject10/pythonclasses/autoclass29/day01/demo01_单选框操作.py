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

xpath_str1 = "/html/body/div[2]/div[2]/div/form/div[3]/label[1]"
xpath_str2 = "/html/body/div[2]/div[2]/div/form/div[3]/label[2]"

radio1 = chromeDriver.find_element(by=By.XPATH, value=xpath_str1)
radio2 = chromeDriver.find_element(by=By.XPATH, value=xpath_str2)

if radio1.is_selected():
    radio2.click()
else:
    radio1.click()