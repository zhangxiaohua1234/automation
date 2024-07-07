#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年05月28日
"""
import random
import requests

# base_url = 'https://httpbin.org'
#
# age = random.randint(18, 25)
# h = random.randint(170, 185)
#
# url0 = base_url + "/get?age=%s" % age
# url1 = base_url + "/get?age=%s&hight=%s" % (age, h)
# url2 = base_url + "/get?age=%(age)s&hight=%(height)s" % {"height": 5, "age": 6}
# url3 = base_url + "/get?age=%(age)s&b=%(b)s" % {"b": random.randint(170, 185), "age": random.randint(18, 25)}
# print(url0)
# print(url1)
# print(url2)
# print(url3)
#
#
# url4 = base_url + "/get?age={}&h={}".format(age, h)
# url4 = base_url + "/get?age={}&h={}".format(random.randint(170, 185), h)
# print(url4)
# url5 = base_url + "/get?age={1}&h={0}".format(age, h)
# url5 = base_url + "/get?age={1}&h={0}&age={1}".format(age, h)
# print(url5)

# url6 = base_url + "/get?age={age}&h={h}".format(age=age, h=h)
# print(url6)


# a = random.randint(0, 10)
# b = random.randint(0, 10)
# base_url = 'https://httpbin.org'
# url = f'{base_url}/get?a={a}&b={b}'
# print(url)

# 没看懂
# import uuid
#
# token = str(uuid.uuid1())
# url = 'https://httpbin.org/get'
# params = {'token': token}
# headers = {'item': '123'}
# headers.setdefault('token', '123')
# headers['token'] = token
# headers.update({'item1': '123', 'item2': '123'})
# res = requests.get(url, params=params, headers=headers)
# print(res.text)


# import random
# import string
#
# list1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王']
# list2 = ['志', '玉', '明', '龙', '芳', '军', '玲', '海']
# list3 = ['', '立', '玲', '', '国', '明', '花']
# list4 = string.ascii_letters + string.digits
# name = random.choice(list1) + random.choice(list2) + random.choice(list3)
# password = ''.join(random.sample(list4, 6))
# print(name, password)


# import faker
# import requests
#
# f = faker.Faker(locale='zh-CN')
# url = 'https://httpbin.org/post'
# data = {'name': f.name(), 'password': f.password(), 'email': f.email()}
# res = requests.post(url, data=data)
# print(res.text)
