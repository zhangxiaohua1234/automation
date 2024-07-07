#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年07月23日
"""
trycount = 0
while trycount < 3:
    use = input("请输入用户名：")
    passwd = input("请输入密码：")
    trycount += 1
    if use == "root":
        if passwd == "2121":
            print("用户登录成功")
            break
        else:
            print("密码错误")
            print("你还有%s次机会" % (3 - trycount))
    else:
        print("用户不存在")
        print("你还有%s机会" % (3 - trycount))
else:
    print("很抱歉，三次机会已经用完，无法再继续登录")