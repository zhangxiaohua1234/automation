#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
from selenium.webdriver.common.by import By

import openchrome
mydriver = openchrome.openTestPage()
mydriver.switch_to.frame("parent_frame")
mydriver.switch_to.frame("left")
mydriver.find_element(by=By.XPATH, value="/html/body/ul/li[2]/a").click()
#因为left和mian 是兄弟，现在已经进入left了，要进入main就得返回到他们的父框架
mydriver.switch_to.parent_frame()
mydriver.switch_to.frame("main")
#可以直接返回到最外层
mydriver.switch_to.default_content()
