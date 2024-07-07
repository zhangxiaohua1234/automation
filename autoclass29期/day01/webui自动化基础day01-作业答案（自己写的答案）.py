#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月06日
"""


### C:\Users\张德宝\tutorial\Scripts\python.exe
#如果浏览器升级了，有一个一劳永逸方法如下：
from webdriver_manager.chrome import ChromeDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
mydriver = webdriver.Chrome()

#打开链接
mydriver.get(r"http://115.28.108.130/newecshop/?u=317")

#打印地址
print(mydriver.current_url)

#精准查找
mydriver.find_element("link text", "请登录").click()

# id查找
mydriver.find_element(by=By.ID, value="username").send_keys("syz")
mydriver.implicitly_wait(30)  #感觉没有生效，怎么回事？

#name 查找
mydriver.find_element(by=By.NAME, value="password").send_keys("123456")

#TAG_NAME
# mydriver.find_elements(by=By.TAG_NAME, value="input")[3].click()    #Message: element not interactable  这个方法没有成功

# CLASS_NAME
mydriver.find_element(by=By.CLASS_NAME, value="checkbox").click()

# XPATH查找 //*[@id="loginsubmit"]
mydriver.find_element(by=By.XPATH, value='//*[@id="loginsubmit"]').click()

#以上是登录成功的操作

#模糊匹配
mydriver.find_element("partial link text", "家").click()

#CSS_SELECTOR  加入购物车
mydriver.find_element(by=By.CSS_SELECTOR, value="#li_114 > div > a.add-cart").click()

# CLASS_NAME   加入购物车
# mydriver.find_element(by=By.CLASS_NAME, value="add-cart").click()

# #后退
# mydriver.back()
# #前进
# mydriver.forward()

#xpath
# mydriver.find_element(by=By.XPATH, value='//*[@id="collectBox"]/div').click()

#打开购物车
mydriver.find_element(by=By.XPATH, value='//*[@id="quick-links"]/ul/li[3]').click()
# mydriver.find_element(by=By.CLASS_NAME, value="right-sidebar-main").click()

se = mydriver.find_element(
    by=By.XPATH, value='/html/body/div[9]/div/div[2]/div[2]').find_element(
    by=By.XPATH, value='//*[@id="formCart"]/div').find_element(
    by=By.XPATH, value='//*[@id="formCart"]/div/div[2]/div').find_elements(
    by=By.TAG_NAME, value='a')
se[0].click()