#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/10/15 11:25
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

import random

base_url = 'https://httpbin.org'

age = random.randint(18, 25)
#
# url = base_url + "/get?age=%s" % age
# print(url)
#
# url = base_url + "/get?age=%(age)s&h=%(h)s" % {"h": random.randint(160, 200), "age": random.randint(15, 40),}
#
# print(url)
#
# url = base_url + "/get?age={}&h={}".format(random.randint(160, 200), 2)
# print(url)
#
# url = base_url + "/get?age={0}&h={0}".format(random.randint(160, 200), 2)
# print(url)
#
# url = base_url + "/get?age={a}&h={h}".format(h=random.randint(160, 200), a=2)
# print(url)

# a = random.randint(160, 200)
# h = 5
# url = base_url + f"/get?age={a}&h={h}"
# print(url)

import uuid

token = str(uuid.uuid1())

params = {
    "token": token
}
headers = {
    "item": "123"
}

headers.setdefault('token', '123')
print(headers)
# headers["token"] = token
headers.update({"item": "456", "token":token})
print(headers)

import random
import string
list1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王']
list2 =['志', '玉','明','龙','芳','军','玲', '海']
list3 =['','立','玲','','国','明', '花']
list4 = string.ascii_letters+string.digits
name = random.choice(list1) + random.choice(list2) + random.choice(list3)
password = ''.join(random.sample(list4, 6))
print(name, password)

import faker
fa = faker.Faker(locale="zh-CN")
print(fa.name(), fa.password(), fa.email())