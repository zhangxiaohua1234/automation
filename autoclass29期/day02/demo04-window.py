#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
from selenium.webdriver.common.by import By
from time import sleep
import openchrome

mydriver = openchrome.openTestPage()

new_window = mydriver.find_element(by=By.ID, value="new_window")
new_window.click()


#获取所有的句柄，通过句柄可以来回切换  新窗口切换
allHandles = mydriver.window_handles
print(allHandles)
mydriver.switch_to.window(allHandles[1])
sleep(5)
mydriver.find_element(by=By.XPATH, value="/html/body/button").click()




#新标签切换
#回到起始窗口
mydriver.switch_to.window(allHandles[0])
#点击在新标签打开百度
new_tips = mydriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/a[2]")
new_tips.click()
#切换到新标签
allHandles = mydriver.window_handles
mydriver.switch_to.window(allHandles[-1])
#定位百度输入框
baidu = mydriver.find_element(by=By.ID, value="kw")
baidu.click()
#输入
baidu.send_keys("宇宙")
#查询
baidu.submit()