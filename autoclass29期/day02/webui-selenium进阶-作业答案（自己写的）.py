#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月18日
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from day01.day0.hanshu import options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

mydriver = webdriver.Chrome()
# op = options(mydriver)
mydriver.get("http://115.28.108.130/newecshop/admin/privilege.php?act=logout")
# mydriver.implicitly_wait(10)
#函数调用方式
# options.name(op, "username").send_keys("test02")
# options.name(op, "password").send_keys("test02")
mydriver.maximize_window()
username = mydriver.find_element(by=By.NAME, value="username")
password = mydriver.find_elements(by=By.CLASS_NAME, value="text_input1")[1]
username.send_keys("test02")
password.send_keys("test02")
checkbox = mydriver.find_element(by=By.ID, value="remember").click()
submit = mydriver.find_element(by=By.CLASS_NAME, value="button2").click()
mydriver.switch_to.frame("menu-frame")

#显示等待(没有成功)
# def find_shangpinguanli(mydriver):
#     return mydriver.find_element(by=By.XPATH, value='//*[@id="menu-frame"]')
#
# WebDriverWait(mydriver=mydriver, timeout=30, poll_frequency=1).until(find_shangpinguanli)
#点击商品管理；此处使用显示等待，不等页面完全加载完毕，页面出现想要点击的元素后即可执行下一步操作   (成功的)
si = WebDriverWait(driver=mydriver, timeout=30, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu-ul"]/li/ul/li[1]/a')))
si.click()
#点击商品管理
# mydriver.find_element(by=By.XPATH, value="//*[text()='商品管理']").click()

sleep(1)
mydriver.find_element(by=By.XPATH, value="//*[text()='商品列表']").click()
#配合函数调用的方式
# WebDriverWait(mydriver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[text()='商品管理']"))).click()
# WebDriverWait(mydriver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[text()='商品列表']"))).click()
# //input[@class="button2"]  #登录页面手写Xpath定位元素
# //*[@class="container"]  #登录后页面手写Xpath定位元素

#点击添加新商品：
mydriver.switch_to.parent_frame()
mydriver.switch_to.frame('main-frame')
mydriver.find_element(by=By.XPATH, value="/html/body/h1/span[1]").click()
#商品名称
mydriver.find_element(by=By.NAME, value="goods_name").send_keys("苹果12")
# #商品货号
mydriver.find_element(by=By.CSS_SELECTOR, value="#general-table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]").send_keys("ECS341341")
# # #商品分类
mydriver.find_element(by=By.ID, value="cat_name").click()
# # #选择分类：手机、数码、通信
mydriver.find_element(by=By.XPATH, value='//*[@id="menuContent_cat_id"]').find_element(by=By.ID, value="treeDemo_cat_id_45_a").click()
#扩展分类：
selector = Select(mydriver.find_element(by=By.NAME, value='other_cat[]'))
selector.select_by_value("4")
#商品品牌：
mydriver.find_element(by=By.ID, value='brand_search').click()
mydriver.find_element(by=By.XPATH, value='//*[@id="ckCK"]/a').click()
# 选择供货商：
selector1 = Select(mydriver.find_element(by=By.NAME, value='suppliers_id'))
selector1.select_by_value('1')
#本店售价
mydriver.find_element(by=By.CSS_SELECTOR, value='#general-table > tbody > tr:nth-child(7) > td:nth-child(2) > input[type=text]:nth-child(1)').send_keys("10000")
sleep(1)
#手机专享价：
mydriver.find_element(by=By.NAME, value='exclusive').send_keys("20000")
sleep(1)
#上传文件
file_btn = mydriver.find_element(by=By.XPATH, value='//*[@id="general-table"]/tbody/tr[19]/td[2]/input[1]')
file_btn.send_keys(r'D:\Dingtalk_20230820000531.jpg')
sleep(1)
#取消勾选商品缩略图勾选框
mydriver.find_element(by=By.ID, value='auto_thumb').click()
sleep(1)
#点击上传图片
picture = mydriver.find_element(by=By.NAME, value='goods_thumb')
picture.send_keys(r'D:\Dingtalk_20230820000531.jpg')
sleep(1)
mydriver.find_element(by=By.ID, value='goods_info_submit').click()

sleep(10)
