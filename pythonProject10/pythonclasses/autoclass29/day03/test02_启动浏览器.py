#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年07月07日
"""
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ChromeOptions
#
#
# def setup_module():
#     print('测试模块开始执行')
#
#
# def setup_function():
#     print('测试方法开始执行')
#
#
# @pytest.fixture
# def setup():
#     # 实例化options对象
#     myoptions = ChromeOptions()
#     # 保持浏览器启动不关闭
#     myoptions.add_experimental_option("detach", True)
#     # 启动浏览器
#     mydriver = webdriver.Chrome(options=myoptions)
#     # 智能等待
#     mydriver.implicitly_wait(10)
#
#     return mydriver
#     # yield mydriver
#     #
#     # mydriver.quit()
#
#
# # driver = ''  #这个没有用到，感觉没用
# def teardown_module():
#     print('模块结束')
#     driver.quit()
#
#
# def test_01(setup):
#     global driver  # 设置全局变量 driver
#     driver = setup  # setup 存到 driver 变量中
#     driver.get(
#         r'D:\python_files\pythonProject10\pythonclasses\autoclass29\selenium_demo\selenium_demo\selenium.html')


# import pytest
# import requests
#
#
# @pytest.fixture(scope='module')
# def http():
#     # 测试准备
#     session = requests.session()
#     session.headers = {'Token': 'abc123'}
#     yield session  # 返回会话
#     # 测试清理
#     session.close()
#
#
# def test_httpbin_get(http):  # fixture 作为参数可以使用
#     res = http.get('https://httpbin.org/get')
#     assert res.status_code == 200


import pytest

DATA = {'user1': '张三', 'user2': '李四'}


# @pytest.fixture
# def get_user():
#     def func(key):  # 定义一个内部功能函数
#         return DATA.get(key)
#
#     return func  # 返回一个函数
#
#
# def test_1(get_user):
#     name = get_user('user1')  # 在用例中使用不同的参数获取不同的数据
#     print(name)
