#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月10日
"""
from appium import webdriver
from appium.options.common.base import AppiumOptions
# from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from caps import Capabilities

mycaps = Capabilities()
mycaps.auto_start_calculators()
# caps = UiAutomator2Options()
# caps.platform_name = "Android"
# caps.automation_name = 'uiautomator2'
# caps.device_name = "127.0.0.1:7555"
# caps.app_package = "com.ibox.calculators"
# caps.app_activity = ".SplashActivity"
# caps.auto_grant_permissions = True  # 是否自动授权，默认为False
# caps.no_reset = True  # 不重置App，保留应用当前状态，默认为False

driver = webdriver.Remote("http://127.0.0.1:4723", options=mycaps.caps)

print(driver.current_package)
print(driver.current_activity)

#
# b1 = driver.find_element(by=AppiumBy.ID, value="com.ibox.calculators:id/digit1")
# print(b1.size)
num = 333

oprate = {".": "dot"}


def add(num):
    for i in str(num):
        if i == ".":
            id = "com.ibox.calculators:id/dot"
        else:
            id = "com.ibox.calculators:id/digit%s" % (i)

        driver.find_element(by=AppiumBy.ID, value=id).click()


add(num)
driver.quit()

