#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import openchrome

mydriver = openchrome.openTestPage()

ele1 = mydriver.find_element(by=By.XPATH, value='//*[@id="draggable"]')
ele2 = mydriver.find_element()

ele1.send.keys(Keys.RETURN)

from selenium.webdriver.common.action_chains import ActionChains

ActionChains(mydriver).click_and_hold(ele1).move_to_element(ele2).perform()

ActionChains(mydriver)