#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年07月12日
"""
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# 登录
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://115.28.108.130/newecshop/user.php")
    yield driver
    driver.quit()
