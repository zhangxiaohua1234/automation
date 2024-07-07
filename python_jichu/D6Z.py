#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年07月23日
"""

# 第六章 Python 文件操作
# 6.1.2 文件的作用
# 就是把一些数据存放起来，可以让程序下一次执行的时候直接使用，而不必重新制作一份，省时省力。
# 6.2 文件的打开与关闭
# 想一想：
# 如果想用 word 编写一份简历，应该有哪些流程呢？
# 1、打开 word 软件，新建一个 word 文件
# 2、写入个人简历信息
# 3、保存文件
# 4、关闭 word 软件

# 6.2.1 写文件：
# f = open("test.txt", "w")
# f.write("hello,大家好")
# f.close()


# 6.2.2 读文件：
# f = open("test.txt", "r", encoding="gbk")
# data = f.read()
# print(data)
# f.close()


# f1 = open("text1.txt", "w", encoding="gbk")
# f1.write("天气真热啊")
# f1.close()

# f1 = open("text1.txt", "r", encoding="gbk")
# data = f1.read()
# print(data)
# f1.close()


# 6.2.3 在本地磁盘读取文件：
# f = open("D:\\test.txt", mode="r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()
#
#
# 追加文件：
# f = open("test.txt", "a", encoding="gbk")
# f.write("巨匠精神")
# f.close()


# f = open("D:\\新建文件夹1\\ceshi.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()




# 6.3.1读数据的区别
# f = open("test.txt", mode="r", encoding="gbk")
# msg = f.read(3)
# msg1 = f.read()
# f.close()
# print(msg)
# print(msg1)

# f = open("test.txt",mode="r", encoding="gbk" )
# con = f.readline()
# print(con)
# con = f.readline()
# print(con)
# con = f.readline()
# print(con)
# f.close()
