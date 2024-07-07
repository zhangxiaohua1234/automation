
#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年06月10日
"""
"""
Python标准库常见模块
操作系统相关:OS
时间与日期:time,datetime
科学计算:math
网络请求:urllib
"""

"""
os模块主要是对文件,目录的操作
常用方法:
os.mkdir()创建目录
os.removedirs()删除文件
os.getcwd()获取当前目录
os.path.exists(dir or file)判断文件或者目录是否存在
"""

import os
import time
# os.mkdir("testdir")
# print(os.listdir("./"))
# # os.removedirs("testdir")
# print(os.getcwd())

# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt", "w")
#     f.write("hell, os using")
#     f.close()
#
# with open("b/test.txt", "r+", encoding = "utf-8") as f:
#     f.write("在马征脸上写")
#     print(f.readline())
#

# print(abs(time()))
# print(time.time())
#
# time.sleep(5)
# print(time.time())
#


