#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年06月12日
"""
from selenium.webdriver.common.by import By
from time import sleep
import openchrome
mydriver = openchrome.openTestPage()
mydriver.find_element(by=By.XPATH, value='/html/body/div[2]/div[5]/div/button').click()
sleep(1)
mydriver.find_element(by=By.XPATH, value='//*[@id="exampleModal"]/div/div/div[1]/button').click()
# alert
mydriver.find_element(by=By.ID, value='alert').click()
print(mydriver.switch_to.alert.text)
sleep(1)
mydriver.switch_to.alert.accept()

# confirm
mydriver.find_element(by=By.ID, value='confirm').click()
sleep(2)
mydriver.switch_to.alert.accept()

mydriver.find_element(by=By.ID, value='confirm').click()
sleep(1)
mydriver.switch_to.alert.dismiss()

sleep(1)
mydriver.find_element(by=By.ID, value='prompt').click()
mydriver.switch_to.alert.send_keys('sdfsdfs')
sleep(1)
mydriver.switch_to.alert.accept()