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
file_btn1 = chromeDriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div[1]/input")
file_btn1.send_keys("D:\新建文本文档.txt")

file_btn2 = chromeDriver.find_element(by=By.XPATH, value='//*[@id="upform"]')
js = 'arguments[0].removeAttribute("style");'
chromeDriver.execute_script(js, file_btn2)

file_btn3 = chromeDriver.find_element(by=By.XPATH, value='//*[@id="upteainput"]')
file_btn3.send_keys("D:\新建文本文档.txt")
input()
12312