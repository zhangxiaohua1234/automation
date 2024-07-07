#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月10日
"""
from appium.options.android import UiAutomator2Options


class Capabilities:
    def __init__(self):
        self.caps = UiAutomator2Options()

    # 自动选择设备，不启动 App
    def auto_select_sevices(self):
        self.caps.platform_name = "Android"
        self.caps.automation_name = "UIAutomator2"

    # 自动安装（或重新安装）应用并启动,高仿微信
    def auto_install_app(self):
        self.caps.platform_name = "Android"
        self.caps.automation_name = "UIAutomator2"
        self.caps.app = r"D:\autocalss\自动化\高仿微信.apk"

    def auto_start_calculators(self):
        self.caps.platform_name = "Android"
        self.caps.automation_name = 'uiautomator2'
        self.caps.device_name = "127.0.0.1:7555"
        self.caps.app_package = "com.ibox.calculators"
        self.caps.app_activity = ".SplashActivity"
        # self.caps.app_package = "com.lqr.wechat"
        # self.caps.app_activity = "com.lqr.wechat.ui.activity.SplashActivity"
        self.caps.auto_grant_permissions = True  # 是否自动授权，默认为False
        self.caps.no_reset = True  # 不重置App，保留应用当前状态，默认为False
        # self.caps.full_reset = True
