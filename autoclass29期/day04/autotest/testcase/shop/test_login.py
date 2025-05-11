#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/8/20 16:16
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz
import logging

from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check
# //*[@id="msg-error-text"]
# asserttype  断言类型  1：查早目标元素 2：获取页面信息 url title 获取特殊的元素属性


#登录
# import logging
from conftest import BASE_DIR
from utils.data_utils import JSON_UTILS
from page.login.login_page_api import login_step

testdata = JSON_UTILS().json_file_load(BASE_DIR.TESTDATA_DIR / "data_login.json")


@pytest.mark.parametrize("user", testdata['testcases'])
def test_login(driver, user):
    logging.info("当前执行用例->"+user["casename"]+"级别->"+user["caselevel"])
    login_step(driver, user=user["username"], passwd=user["password"])

    # print("当前执行用例->", user["casename"], "级别->", user["caselevel"])
    # sleep(0.5)
    # print("开始断言", user["expected"])
    # res_ele = driver.find_element(by=testdata["eletype"], value=testdata["elepath"])

    if user['asserttype'][0] == "fe":
        res_ele = WebDriverWait(driver, 10, 1).\
               until(EC.visibility_of_element_located((user["asserttype"][1], user["elepath"])))
        # print(res_ele.text)
        res = pytest_check.assert_equal(res_ele.text, user["elecontext"], msg=user["expected"])
        if res:
            logging.info("用例执行成功->期望结果是：" + user["elecontext"]+"实际结果是："+ res_ele.text)
            driver.save_screenshot(str(BASE_DIR.TESTLOGS_DIR) + "/screenshot/" + user["casename"] + ".png")
        else:
            logging.info("用例执行失败->期望结果是：" + user["elecontext"] + "实际结果是：" + res_ele.text)
            driver.save_screenshot(str(BASE_DIR.TESTLOGS_DIR) + "/screenshot/"+user["casename"]+".png")

    elif user['asserttype'][0] == "new_url":
        res = pytest_check.is_true(EC.url_to_be(user["elecontext"]))
        if res:
            logging.info("用例执行成功->期望结果是：" + user["elecontext"]+"实际结果是：" + driver.current_url)
        else:
            logging.info("用例执行失败->期望结果是：" + user["elecontext"] + "实际结果是：" + driver.current_url)
            driver.save_screenshot(str(BASE_DIR.TESTLOGS_DIR) + "/screenshot/" + user["casename"] + ".png")