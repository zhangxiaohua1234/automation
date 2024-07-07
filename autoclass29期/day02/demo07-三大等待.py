#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月13日
"""
#强制等待
#职能等待
#显示等待 条件等待 等待某个逻辑的发生或者结果， 才去执行，用它可以个性化的定制一些自动化等待逻辑 调教效率
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openchrome
mydriver = openchrome.openTestPage()

#/html/body/div[2]/div[4]/div/table/tbody/tr[3]/td[4]/a

def find_wangwu_chakan(driver):
    return mydriver.find_element(by=By.XPATH, value="/html/body/div[2]/div[4]/div/table/tbody/tr[3]/td[4]/a")
WebDriverWait(driver=mydriver, timeout=30, poll_frequency=1).until(find_wangwu_chakan)

#
# wangwu = WebDriverWait(driver=mydriver, timeout=30, poll_frequency=1).\
#     until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div/table/tbody/tr[3]/td[4]/a")))
# wangwu.click()36