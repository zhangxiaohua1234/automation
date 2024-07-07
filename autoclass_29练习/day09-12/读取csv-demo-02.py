#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/10/15 13:42
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz


"SSS".find()

import csv

# 读取数据
with open('params.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

# 数据写入csv

header = ['name', 'passwd', 'status']
data = [
    ['syz', '123456', 'PASS'],
    ['小明', 'hhh333', 'PASS'],
    ['张#abc123', '123456', 'PASS'],
    ['666', '123456', 'PASS'],
    ['a b', '123456', 'PASS']
]
with open('params.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

with open('params.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['name'], row['passwd'])

header = ['name', 'password', 'status']

data = [
    {'name':'abc', 'password':'123456', 'status': 'FAIL'},
    {'name':'张五', 'password':'123#456', 'status': 'FAIL'},
    {'name':'张#abc123', 'password':'123456', 'status': 'FAIL'},
    {'name':'666', 'password':'123456', 'status': 'FAIL'},
    {'name':'a b', 'password':'123456', 'status': 'FAIL'}
]

with open('params.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    writer.writerows(data)


