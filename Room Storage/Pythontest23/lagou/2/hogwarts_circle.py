#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年06月06日
"""
"""
1、计算1~100 求和
2、加入分支结构实现1~100之间的偶数求和
3、使用python实现1~100之间的偶数求和
"""
# 1、计算1~100 求和
# result = 0
# for i in range(101):
#     print(i)
#     result = result + i
# print(result)

# 2、加入分支结构实现1~100之间的偶数求和
# result = 0
# for i in range(101):
#     print(i)
#     if i%2 == 0:
#         result = result + i
# print(result)


# 3、使用python实现1~100之间的偶数求和
result = 0
for i in range(2, 101, 2):
    result = result + i
print(result)
