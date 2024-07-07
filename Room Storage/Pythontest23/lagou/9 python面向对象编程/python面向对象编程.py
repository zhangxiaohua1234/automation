#  -*- coding:utf-8 -*-
import os
import urllib
"""
作者：张德宝
日期：2023年06月10日
"""
"""
什么是面向对象？
1.语言层面，封装代码和数据
2.规格层面，对象是一系列可被使用的公共接口
3.概念层面，对象是某种拥有责任的抽象
"""

"""
类、实例、方法、变量
类(Class):抽象的概念,一类事物。
方法:类中定义的函数,对外提供的服务。------对外提供的接口
类变量:类变量在整个实例化的对象中是公用的。
实例引用:实例化一个对象
实例变量:以'self.变量名'的方式定义的变量
"""
# 创建一个人类
# 通过 class 关键字，进行定义了一个类
# 定义类是为了实例化一个实例


class Person:
    # 类变量
    name = 'default'
    age = 0
    gender = "male"
    weight = 0
    book = 'python'

    def __init__(self, name, age, gender, weight):
        # self.变量名的方式，访问的变量，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # def set_param(self, name):
    #     self.name = name
    #
    # def set_age(self, age):
    #     self.age = age

    @classmethod
    def eat(self):
        print(f"{self.name}:eating")
        print("xxxxx")

    def play(self):
        print(f"{self.name}:playing")

    def jump(self):
        print(f"{self.name}:jump")


# 怎么实例化一个类呢，通过 class 的名字 Person() 来进行实例化
# 类的实例化，创建实例
zs = Person("张三", 20, "男", 130)
zs.eat()
# zs.set_param('张三')
# zs.set_age('20')
print(f"zhangsan 的姓名是:{zs.name}, zhangsan 的年龄是:{zs.age}, 性别是：{zs.gender}, 体重是：{zs.weight}")

ls = Person("李四", 25, "女", 150)
ls.play()
ls.jump()
print(f"李四     的姓名是:{ls.name}, 李四     的年龄是:{ls.age}, 李四性别是：{ls.gender}, 李四体重是：{ls.weight}")


# 类变量和实例变量的区别，类变量需要使用类来访问；实例变量需要使用实例来访问
# 访问类变量
print(Person.name)
# 访问实例变量
print(zs.name)

# 修改类变量值
Person.name = "default修改成：lili"
print(Person.name)
# 修改实例变量值
zs.name = "张三 修改成：didi"
print(zs.name)


# 类方法和实例方法的区别，类方法使用类.方法进行访问；实例方法使用实例.方法进行访问
# 类不能直接访问 实例方法，需要加@classmethod ，加了装饰器之后就可以访问类方法
Person.eat()
