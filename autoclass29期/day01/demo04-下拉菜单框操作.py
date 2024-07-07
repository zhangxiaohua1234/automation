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


select_menu = mydriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/form/div[5]")

select_menu.click()

se = mydriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/form/div[5]/div").find_elements(by=By.TAG_NAME, value="a")


se[0].click()


input()