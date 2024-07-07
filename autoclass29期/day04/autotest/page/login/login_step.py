#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月27日
"""

from selenium.webdriver.common.by import By
from page.base_page import BasePage


def login_step(driver, user, passwd):
    BP = BasePage(driver)
    username = BP.find_element(by=By.ID, value="username")
    password = BP.find_element(by=By.ID, value="password")
    login = BP.find_element(by=By.CLASS_NAME, value='login-btn')
    username.send_keys(user)
    password.send_keys(passwd)
    login.click()
