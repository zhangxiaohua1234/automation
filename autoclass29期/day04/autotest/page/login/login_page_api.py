#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月27日
"""
from selenium.webdriver import Chrome
from page.login.login_step import login_step


class LoginPage:

    @staticmethod
    def login_step(driver: Chrome, user, passwd):
        login_step(driver, user, passwd)

    def resign_step(self):
        pass

    def find_passwd_step(self):
        pass
