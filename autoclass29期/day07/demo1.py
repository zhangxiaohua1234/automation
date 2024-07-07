#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月17日
"""
from appium import webdriver
from day07.appautotest.utils.caps import Capabilities

mycaps = Capabilities()
mycaps.auto_start_calculators()

mydriver = webdriver.Remote("http://127.0.0.1:4723", options=mycaps.caps)
mydriver.toggle_location_services()

devces_info = {}

devces_info["battery_info"] = mydriver.battery_info
devces_info["device_time"] = mydriver.device_time
devces_info["get_window_size"] = mydriver.get_window_size()
devces_info["network_connection"] = mydriver.network_connection
print(devces_info)

mydriver.keyevent(8)
mydriver.long_press_keycode(8,6)

# ele = mydriver.find_element("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[4]")
# TouchAction(mydriver).press(ele).wait(6000).perform()
print(mydriver.contexts)

mydriver.quit()