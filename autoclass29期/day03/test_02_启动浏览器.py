#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月20日
"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# def setup():
#     myoptions = ChromeOptions()
#     myoptions.add_experimental_option("detach", True)
#     mydriver = webdriver.Chrome(options=myoptions)
#     mydriver.implicitly_wait(5)
#     mydriver.get(r"D:\autoclass29期\selenium_demo\selenium_demo\selenium.html")
#
#     return mydriver


def setup_module():
    print("测试模块开始执行")


def setup_function():
    print("测试方法开始执行")


@pytest.fixture
def setup():
    # 实例化options对象
    myoptions = ChromeOptions()
    # 保持浏览器启动不关闭
    myoptions.add_experimental_option("detach", True)
    # 启动浏览器
    mydriver = webdriver.Chrome(options=myoptions)
    # 智能等待
    mydriver.implicitly_wait(1)

    mydriver.get(r"D:\autoclass29期\selenium_demo\selenium_demo\selenium.html")

    return mydriver
    # yield mydriver
    #
    # mydriver.quit()

driver = ""
def teardown_module():
    print("模块结束")
    driver.quit()


def test_01(setup):
    global driver
    driver = setup
    setup.get(r"D:\autoclass29期\selenium_demo\selenium_demo\selenium.html")