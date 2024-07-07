#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/2 14:11
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz
'''
1、给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个
整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
'''

from selenium.webdriver.common.by import By
import random

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i,j]

'''
2、实现商城前台登录  账户：syz， 密码：123456
登陆成功后，将一件商品加入购物车
3、拓展：有能力的完成下单。
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://115.28.108.130/newecshop/user.php")
#登录
username = driver.find_element(by=By.ID, value="username")
password = driver.find_element(by=By.ID, value="password")
login = driver.find_element(by=By.CLASS_NAME, value='login-btn')

username.send_keys("syz")
password.send_keys("123456")
login.click()

sleep(2)
#由于默认进入的是个人中心，点一下图标进入上商城首页
driver.find_element(by=By.XPATH , value = '/html/body/div[2]/div/div[1]/a/img').click()

# tips = driver.window_handles
# driver.switch_to.window(tips[1])

#选择分类
shopType = driver.find_elements(by=By.CLASS_NAME, value="list")
target = random.choice(shopType)

targetType = target.find_element(by=By.CLASS_NAME, value="cat-name")
targetType.click()

#由于是打开了一个新的标签页，需要切换到这个新的标签页
tips = driver.window_handles
driver.switch_to.window(tips[1])

#获取所有商品
shops = driver.find_elements(by=By.CLASS_NAME, value="add-cart")

#页面中可能没商品，有商品才选择一个商品加入购物车
if len(shops) > 0:
    shop = random.choice(shops).click()

#打开购物车

driver.find_element(by=By.ID, value="collectBox").click()

#点击去结算

driver.execute_script("$(arguments[0]).click()", driver.find_element(by=By.LINK_TEXT, value="去购物车结算"))








