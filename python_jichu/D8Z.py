#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年07月30日
"""


# import daorulianxi
# daorulianxi.test1()
# daorulianxi.test2()


# from daorulianxi import test1, test2
# test1()
# test2()


# from daorulianxi import *
# test1()
# test2()



# import aaa.test_a
# aaa.test_a.func1()
# aaa.test_a.func2()


# from aaa.test_a import func1
# func1()


# from aaa.test_a import *
# func1()
# func2()



# 8.2 常用模块介绍
# 8.2.1 time

import time
# time.sleep(5)
# print("我是一只小小鸟")

# print(time.time())#时间戳
# print(time.localtime())#本地时区的 struct_time
# print(time.strftime("%Y-%m-%d %H:%m:%S"))# 格式化的时间字符串
# print(time.strftime("%Y-%m-%d %X"))# 格式化的时间字符串



# 8.2.2 random 模块
# import random
# print(random.random())#(0,1)----float 大于 0 且小于 1 之间的小数
# print(random.randint(1, 3))#[1,3] 大于等于 1 且小于等于 3 之间的整数
# print(random.randrange(1, 3))#[1,3) 大于等于 1 且小于 3 之间的整数
# print(random.choice([1, "23", [4, 5]]))#随机选择一个进行输出



# 8.3 命名空间
# a = 3
# def func():
#     a = 1
#     print(a)
#
#
# func()


# count = 3
# def func1():
#     global count #生命全局变量
#     count += 1
#     print(count)
#
#
# func1()



# 8.5 异常定义:
# print(a)


# 8.5.2 异常的基本语法

# 捕获异常 try...except...
# try:
#     可能发⽣错误的代码
# except:
#     如果出现异常执⾏的代码


# try:
#     open("tat.txt")
# except FileNotFoundError:
#     print("我捕获了异常")




# 8.5.3 捕获多个指定异常

# try:
#     open("test01.txt")#FileNotFoundError
#     print(num)#NameError
#     print("--11--")
# except (FileNotFoundError, NameError):
#     print("有错误")


#
# 8.5.5 获取异常的信息描述
# try:
# print(a)
# except Exception as ret:
# print(ret)


# 异常的 else
# try:
# print(1)
# except Exception as result:
# print(result)
# else:
# print('我是 else，是没有异常的时候执⾏的代码')







# 第九章 面向对象编程介绍

# 9.1 类和对象

# 9.1.1 类
# 人以类聚 物以群分。
# 具有相同属性和行为事物的统称
# 相似内部状态和运动规律的实体的集合(或统称为抽象)。
# 类是抽象的,在使用的时候通常会找到这个类的一个具体的存在,使用这个具体的存在。一个类可以找到
# 多个对象。


# 9.1.2 对象
# 某一个具体事物的存在 ,在现实世界中可以是看得见摸得着的。
# 可以是直接使用的


# 9.1.4 类的构成
# 类(Class) 由 3 个部分构成：
# 类的名称:类名
# 类的属性:一组数据（固定的、信息）
# 类的方法:允许对进行操作的方法 (行为)；拥有的功能就是方法
# 举例：
# 1）人类设计,只关心 3 样东西:
# 事物名称(类名):人(Person)
# 属性:身高(height)、年龄(age)
# 方法(行为/功能):跑(run)、打架(fight)

# 定义类：
# def xxx():
# <1>定义一个类，格式如下：
# class 类名:
# 方法列表





# 个人理解类的方法就是：类可以做哪些事情




# class wangcai:#类名
#     #属性
#     #方法
#     def eat(self):
#         print("猫在吃鱼")
#
#     def drink(self):
#         print("猫在喝水")
#
#     def play(self):
#         print("猫咪在玩耍")
#
# #创建对象
# tom =  wangcai()
# tom.eat()
# tom.drink()
# tom.play()
#
# #添加属性就是添加变量
# tom.name = "汤姆"
# tom.age = 40
# #打印属性
# print(tom.name)
# print(tom.age)






# # Self
# # <1>从创建多个对象引入 self
# class wangcai:#类名
#     #属性
#     #方法
#     def eat(self):
#         print("猫在吃鱼")
#
#     def drink(self):
#         print("猫在喝水")
#
#     def play(self):
#         print("猫咪在玩耍")
#
#     def introuce(self):
#         print("%s的年龄是:%d" % (self.name, self.age))
# #创建对象
# tom =  wangcai()
# tom.eat()
# tom.drink()
# tom.play()
#
# #添加属性就是添加变量
# tom.name = "汤姆"
# tom.age = 40
# #tom 自我介绍
# tom.introuce()
# #打印属性
# # print(tom.name)
# # print(tom.age)
#
#
# #创建第二个对象
# lanmao = wangcai()
# #添加属性就是添加变量
# lanmao.name = "蓝猫"
# lanmao.age = 10
# #tom 自我介绍
# lanmao.introuce()
#





# # 再次加深理解 self（扩展）
# # self 是指调用该函数的对象
# # 定义类
# class wangcai():
#     def eat(self):
#         print("猫会叫")
#         print(self) # 研究 self 是什么？
# #2. 创建对象
# jiao = wangcai() #jiao 对象拥有 eat 里面所有的属性和方法
# print(jiao)
# # 3.用 jiao 对象调用 eat 函数
# jiao.eat()





# 第二个知识点:
# 在 Python 中， __xx__() 的函数叫做魔法⽅法，指的是具有特殊功能的函数。
# __init__() ⽅法的作⽤：初始化对象。
# init 方法：
# __init__()方法


# <2>使用方式
# 方式
# class 类名:
    #初始化函数，用来完成一些默认的设定
# class dog:
#     #初始化函数，用来完成一些默认的设定
#     def __init__(self):
#         print('---1----')
#
# a = dog()



# # init 方法使用场景
# # 需求添加蓝猫对象 和打印蓝猫属性
# class wangcai():
#     def __init__(self, new_name, new_age):
#         self.name = new_name
#         self.age = new_age
# #创建Tom对象
# Tom = wangcai("汤姆", 40)
# print(Tom.name)
# print(Tom.age)
#
#
# #创建lanmao对象
# lanmao = wangcai("蓝猫", 20)
# print(lanmao.name)
# print(lanmao.age)





# class wangcai:
# def __init__(self, name, age):
# # 在__init__方法最先执行，代码相当于定义 name 并赋值
# self.name= name
# self.age= age
# def eat(self):
# print('猫在吃鱼...')
# # 创建对象
# tom= wangcai("汤姆",40)
# print("%s 的年龄是%d"%(tom.name,tom.age))



# 9.2 面向对象特性讲解
# 9.2.1 面向对象继承
# 一、继承
# class Animal:
#     def eat(self):
#         print("吃")
#     def drink(self):
#         print("喝")
#     def sleep(self):
#         print("睡")
#
# class wangcai(Animal):
#     def run(self):
#         print("玩")
#     def back(self):
#         print("喵喵")
#
# a = Animal()
# a.eat()
# a.drink()
# a.sleep()
#
#
# wangcai = wangcai()
# wangcai.eat()
# wangcai.drink()
# wangcai.sleep()
# wangcai.run()
# wangcai.back()




#多层继承
# class Animal:
#     def eat(self):
#         print("吃")
#     def sleep(self):
#         print("睡")
#
# class Dog(Animal):
#     def eat(self):
#         print("吃-1")
#     def sleep(self):
#         print("睡-1")
#
# class XiaoTQ(Dog):
#     def fly(self):
#         print("起飞了")
#
# xtq = XiaoTQ()
# xtq.fly()
# xtq.sleep()



# 三、多继承
# class A:
#     def test1(self):
#         print("--A--")
#
# class B:
#     def test2(self):
#         print("--B--")
#
# class C(A, B):
#     def printC(self):
#         print("--C--")
#
#
# c = C()
# c.test1()
# c.test2()
# c.printC()

# 9.3 面向对象第二部分：封装

class Dog:
    def __test1(self):
        print("aa")
    def test2(self):
        print("bb")


dog = Dog()
dog.test1()
dog.test2()