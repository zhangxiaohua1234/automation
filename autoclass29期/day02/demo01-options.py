#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions

myoptions = ChromeOptions()
#无图模式
myoptions.headless = True


#指定浏览器地址
myoptions.binary_location = r"C:\Program Files\Google\Chrome\Application"
mydriver = webdriver.Chrome(options=myoptions)