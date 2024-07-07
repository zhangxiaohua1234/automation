#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
from selenium.webdriver.common.by import By

import openchrome
import datetime
mydriver = openchrome.openTestPage()

#移除属性js
js = 'arguments[0].removeAttribute("onkeydown")'
date001 = mydriver.find_element(by=By.ID, value="date001")
mydriver.execute_script(js, date001)
date001.click()

now = datetime.datetime.now()
nowYMD = now.strftime("%Y-%m-%d")
print(nowYMD)
date001.send_keys(nowYMD)

#移除属性js
js = 'arguments[0].removeAttribute("onkeydown")'
date002 = mydriver.find_element(by=By.ID, value="date002")
mydriver.execute_script(js, date002)
date002.click()

now = datetime.datetime.now()
nowYMD = now.strftime("%Y-%m-%d%H:%M")
print(nowYMD)
date002.send_keys(nowYMD)