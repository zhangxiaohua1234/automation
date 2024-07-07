#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
from selenium.webdriver.common.by import By
from time import sleep
import openchrome

mydriver = openchrome.openTestPage()

#div框
mydriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[5]/div/button").click()
sleep(1)#强制等待
mydriver.find_element(by=By.XPATH, value='//*[@id="exampleModal"]/div/div/div[3]/button[1]').click()

#alert
mydriver.find_element(by=By.ID, value="alert").click()
print(mydriver.switch_to_alert)
mydriver.switch_to.alert.accept()

#confirm
sleep(2)
mydriver.find_element(by=By.ID, value="confirm").click()
print(mydriver.switch_to_alert)
mydriver.switch_to.alert.accept()

#点击取消
sleep(2)
mydriver.find_element(by=By.ID, value="confirm").click()
print(mydriver.switch_to_alert)
mydriver.switch_to.alert.dismiss()

#prompt
sleep(5)
mydriver.find_element(by=By.ID, value="prompt").click()
print(mydriver.switch_to_alert)
mydriver.switch_to.alert.send_keys("okk")
mydriver.switch_to.alert.accept()

