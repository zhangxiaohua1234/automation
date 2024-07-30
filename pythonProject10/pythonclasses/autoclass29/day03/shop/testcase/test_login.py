#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年07月12日
"""
from time import sleep

import pytest
import pytest_check
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  asserttype 断言类型 1：查找元素目标 2：获取页面信息  url title 获取特殊的元素属性
testdata = [
    {
        'casename': '执行登录-无效用户',
        'caselevel': 'p3',
        'username': 'syz',
        'password': '123456',
        'expected': '用户登录失败',
        'asserttype': ['fe', By.XPATH],
        'elepath': '//*[@id="msg-error-text"]',
        'elecontext': '用户名或密码错误'
    },
    {
        'casename': '执行登录-有效用户',
        'caselevel': 'p0',
        'username': 'zdb123',
        'password': '123456',
        'expected': '用户登录成功',
        'asserttype': ['new_url', ''],
        'elepath': '',
        'elecontext': 'http://115.28.108.130/newecshop/user.php?act=account_detail'
    },
    {
        'casename': '执行登录-密码为空',
        'caselevel': 'p3',
        'username': 'syz',
        'password': '',
        'expected': '用户登录失败',
        'asserttype': ['fe', By.XPATH],
        'elepath': '//*[@id="msg-error-text"]',
        'elecontext': '请输入密码'
    },
]

import logging

@pytest.mark.parametrize('user', testdata)
def test_login(driver, user):
    logging.info('当前执行用例->', user['casename'], '级别->', user['caselevel'])
    print('当前执行用例->', user['casename'], '级别->', user['caselevel'])
    username = driver.find_element(by=By.ID, value="username")
    password = driver.find_element(by=By.ID, value="password")
    login = driver.find_element(by=By.CLASS_NAME, value='login-btn')

    username.send_keys(user['username'])
    password.send_keys(user['password'])
    login.click()
    sleep(0.5)
    logging.info('开始断言', user['elecontext'])
    print('开始断言', user['elecontext'])
    # res_ele = driver.find_element(by=testdata['eletype'], value=testdata['elepath']).text
    if user['asserttype'][0] == 'fe':
        res_ele = WebDriverWait(driver, 10, 1).until(
            EC.visibility_of_element_located((user['asserttype'][1], user['elepath'])))
        # print(res_ele.text)
        pytest_check.assert_equal(res_ele.text, user['elecontext'], msg=user['expected'])
    elif user['asserttype'][0] == 'new_url':
        pytest_check.is_true(EC.url_to_be(user['elecontext']))