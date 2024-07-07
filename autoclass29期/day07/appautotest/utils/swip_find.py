#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月17日
"""
from appium import webdriver
from selenium.common.exceptions import NoSuchFrameException

def bottom_top_swip_find(driver:webdriver.Remote, ele: tuple):

    size = driver.get_window_size()
    width, height = size['width'], size['height']
    start_x = 0.5 * width
    start_y = 0.1 * height

    end_x = start_x
    end_y = height * 0.1

    while True:
        try:
            element = driver.find_element(by=ele[0], value=ele[1])
            return element
        except NoSuchFrameException as e:
            driver.swipe(start_x, start_y, end_x, end_y)