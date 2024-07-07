#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年07月23日
"""

# 第七章Python函数式编程
# 7.2定义函数和调用

# def test():
#     print("*" * 50)
#     print("我是一只小小鸟")
#
# def print_info():
#     print("-" * 50)
#     print("名片登录系统")
#     print("人生苦短，我用Python")
#     print("登录")
#     print("退出")
#     print("_" * 50)
#
# test()
# print_info()



# 7.3 定义函数的三种形式
# 7.3.1有参函数
# def my_max(x, y):
#     if x > y:
#         print(x)
#     else:
#         print(y)
#
#
# my_max(5, 4)
#


# 7.4 函数返回值
# def func():
#     print("--1--")
#     print("--2--")
#     return
#     print("--3--")
# func()
# print(func())
#
# def add2num():
#     a = 11
#     b = 22
#     c = a + b
#     e = "ss"
#     return c
# print(type(add2num()))

# 7.4.2 定义带有参数的函数
# def add3num(a, b):
#     c = a + b
#     print("%d+%d=%d" % (a, b, c))
# num1 = int(input("请输入第一个数"))
# num2 = int(input("请输入第二个数"))
#
# add3num(num1, num2)


# 7.4.3 函数返回多个值
# def test():
#     a = 11
#     b = 22
#     c = 33
#     d = [a, b, c]
#     return d
#
#
# num = test()
# print(num)



# # 函数嵌套调用
# def test1():
#     pass
# def test2():
#     print("--2-1--")
#     print("--2-2--")
# def test3():
#     print("--3-1--")
#     test2()
#     print("--3-2--")
# test3()


# 7.5 函数的位置参数
# def user_info(name, age):
#     print(f"您的名字是{name},年龄是{age}")
# user_info("tom", 30)


# 7.5.2 缺省参数
# def test(a, b=44):
#     result = a+b
#     print("result = %d" % result)
# test(11)
# test(11,6)

# def test(a,b=22,c=33): # 缺省参数只能放在后面定义
# print(a)
# print(b)
# print(c)
# test(11,c=44)
# 报错了


# 7.6.3 动态参数
# def study(*args):
#     print("老吴教你学python", args)
# study("python", "fal", "wer")

# 7.6.4 关键字参数
# def func(**kwargs):
#     print(kwargs)
# func(name = "老吴", sex = "男")