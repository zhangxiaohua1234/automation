#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年06月02日
"""
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriver
from selenium.webdriver.common.by import By
from time import sleep

mydriver = webdriver.Chrome()

mydriver.get("D:\python_files\pythonProject10\selenium_demo\selenium_demo\selenium.html")

# mydriver.implicitly_wait(5)
# # 精确匹配By.LINK_TEXT  模糊匹配 By.PARTIAL_LINK_TEXT
#
# print(mydriver.current_url)
# mydriver.find_element("link text", "百度").click()
# print(mydriver.current_url)
#
# # mydriver.find_element("PARTIAL_LINK_TEXT", "百").click()     模糊匹配没有成功
#
# mydriver.back()
#
# # mydriver.find_element(by=By.CLASS_NAME, value="btn btn-secondary").click()
#
# # id查找
# mydriver.find_element(by=By.ID, value="account").send_keys("你好！")
#
# # name查找
# mydriver.find_element(by=By.NAME, value="account").send_keys("你好2")  # 没有成功
#
# # tag_name查找
# mydriver.find_elements(by=By.TAG_NAME, value="input")[1].send_keys("你好3")

# # XPATH查找
# for i in range(10):
#     xpath_str = "/html/body/div[2]/div[2]/div/form/div[3]/label"
#     xpath_str += "[" + str(i % 2 + 1) + "]"
#     mydriver.find_element(by=By.XPATH, value=xpath_str).click()
#     sleep(2)
# input()


mydriver.get("D:\python_files\pythonProject10\selenium_demo\selenium_demo\selenium.html")

mydriver.implicitly_wait(2)
# 链接文本查找link text 精准匹配
# mydriver.find_element("link text", "百度").click()

print(mydriver.current_url)
# 链接文本查找partial link text 模糊匹配
mydriver.find_element("partial link text", "百").click()
print(mydriver.current_url)

# 返回
mydriver.back()
mydriver.implicitly_wait(2)
mydriver.forward()
sleep(2)
mydriver.back()

# 类型查找 By.CLASS_NAME
# mydriver.find_element(By.CLASS_NAME, value="btn btn-secondary").click()

# Id 查找
# mydriver.find_element(By.ID, value="account").send_keys("hello")

# xpath
mydriver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/form/div[3]/label[1]").click()

# for i in range(10):
#     xpath_str = "/html/body/div[2]/div[2]/div/form/div[3]/label"
#     xpath_str += "[" + str(i % 2 + 1) + "]"
#     mydriver.find_element(by=By.XPATH, value=xpath_str).click()
#     sleep(2)

mydriver.find_element(by=By.CSS_SELECTOR, value="body > div.container > div:nth-child(2) > div > form > div:nth-child(8) > div:nth-child(1) > label").click()

input()