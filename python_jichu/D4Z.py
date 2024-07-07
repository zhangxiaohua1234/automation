#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年07月16日
"""


# if 语句的应用-进阶版
# age =int( input("请输入您的年龄："))
# if age >= 18:
#     print(f"您的年龄是{age}，可以上网！！！！")
# print("系统关闭")


# 4.2.3 if...else..
# age =int( input("请输入您的年龄："))
# if age >= 18:
#     print(f"您的年龄是{age}，可以上网！！！！")
# else:
#     print(f"您的年龄是{age}，不可以上网！！！！")
# print("系统关闭")


# 4.2.4 if 条件判断-多重判断语法
# age = int(input("请输入您的年龄："))
# if age < 18:
#     print(f"您的年龄是{age},不合法")
# elif 18 < age <= 60:
#     print(f"您的年龄是{age},合法年龄")
# elif age > 60:
#     print(f"您的年龄是{age},退休年龄")


# 4.2.5 if 嵌套的格式
# sex = input("请输入性别：")
# if sex == "女":
#     color = input("你白吗？")
#     money = input("请输入你的财产总数：")
#     beautiful = input("你美吗？")
#     if color == "白" and money > "1000" and beautiful == "美":
#         print("白富美")
#     else:
#         print("你还得努力")
#
# elif sex == "男":
#     hight = input("你高吗？")
#     money = input("请输入你的财产总数：")
#     shuai = input("你帅吗？")
#     if hight == "高" and money > "1000" and shuai == "帅":
#         print("高富帅")
#     else:
#         print("你还得努力····")
# else:
#     print("你是火星人")


# pass 关键字的作用
# pass 不做任何事情，一般用做占位语句
# age = 18
# if age > 18:
#     pass


# 4.3 while 循环
# i = 0
# while i < 10:
#     print("我错了")
#     i += 1
# print("原谅你了")

# i = 1
# while i < 10:
#     if i % 2 == 0:
#         print("偶数")
#     else:
#         print("奇数")
#     i += 1

# j = 8
# while j <= 10:
#     i = 1
#     while i <= 5:
#         print("*", end="")
#         i += 1
#     j += 1
#     print("")


# 4.4 for 循环的格式
# name = [1, 2, 3, 4, 5]
# for a in name:
#     print("----")
#     print(a)


# 写的不对
# dict_data = {"key": "小明", "key2": "小张", "key3": "小五"}
# for x in dict_data:
#     print("----")
#     if x == {"key2": "小张"}:
#         break
#     print(x)

# dict_data = "woshiyigehaoren"
# for x in dict_data:
#     print("----")
#     if x == "h":
#         break
#     print(x)


# i = 0
# while i < 10:
#     i += 1
#     print("----")
#     if i == 5:
#         break
#     print(i)


#
# name = "python"
# for x in name:
#     print("---")
#     if x == "t":
#         continue
#     print(x)


# i = 0
# while i < 10:
#     i += 1
#     print("---")
#     if i == 5:
#         continue
#     print(i)


# i = 0
# while i <= 3:
#     i += 1
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     print("登录成功")
#     if i > 3:
#
# i = 1
# while i < 4:
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     if name == "root" and password == "admin123":
#         print("登录成功")
#         break
#     elif i == 3:
#         print("错误次数达到3次，请稍后再试")
#     else:
#         print("用户或密码不正确")
#     i += 1

# for i in range(3):
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     if name == "root" and password == "admin123":
#         print("登录成功")
#         break
#     elif i == 2:
#         print("错误次数达到3次，请稍后再试")
#     else:
#         print("用户或密码不正确")
#     i += 1


# def login(login_name, login_password, i=1):
#     while True:
#         name = input("请输入用户名：")
#         password = input("请输入密码：")
#         if name == login_name and password == login_password:
#             return print("登录成功")
#         elif i == 3:
#             return print("错误次数达到3次，请稍后再试")
#         else:
#             print("用户或密码不正确")
#         i += 1


