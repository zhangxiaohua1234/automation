#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月06日
"""


### C:\Users\张德宝\tutorial\Scripts\python.exe

from selenium.webdriver.common.by import By

# from selenium import webdriver
#
# # from webdriver_manager.chrome import webdriver
#
# mydriver = webdriver.Chrome()
#
# input()


from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriver

from webdriver_manager.chrome import ChromeDriverManager
#   硬编码

# from selenium.webdriver.chrome.service import Service
#
# mys = Service(executable_path=ChromeDriverManager().install())

mydriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

mydriver.get(r"D:\autoclass29期\selenium_demo\selenium_demo\selenium.html")


mydriver.implicitly_wait(5)
#精确匹配By.LINK_TEXT  模糊匹配 By.PARTIAL_LINK_TEXT

print(mydriver.current_url)
mydriver.find_element("link text", "百度").click()
print(mydriver.current_url)

# mydriver.find_element("PARTIAL_LINK_TEXT", "百").click()     模糊匹配没有成功

mydriver.back()



# mydriver.find_element(by=By.CLASS_NAME, value="btn btn-secondary").click()

#id查找
mydriver.find_element(by=By.ID, value="account").send_keys("你好！")

#name查找
mydriver.find_element(by=By.NAME, value="account").send_keys("你好2")                #没有成功

# tag_name查找
mydriver.find_elements(by=By.TAG_NAME, value="input")[1].send_keys("你好3")

# XPATH查找
# xpath_str = "/html/body/div[2]/div[2]/div/form/div[3]/label"
# for i in range(10):
#     xpath_str += "["+ str(i % 2 + 1) + "]"
#     print(xpath_str)
# mydriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/form/div[3]/label[1]/input").click()


