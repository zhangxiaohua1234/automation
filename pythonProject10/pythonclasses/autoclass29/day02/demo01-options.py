#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年06月10日
"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions

myoptions = ChromeOptions()
# 无图模式
# myoptions.add_argument("--headless")
# 指定浏览器运行
# myoptions.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# # 启动浏览器后不自动关闭，方便调试
# myoptions.add_experimental_option("detach", True)
# myoptions.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 8'})
myoptions.add_argument('start-fullscreen')
mydriver = webdriver.Chrome(options=myoptions)
mydriver.get('https://www.baidu.com')

input()