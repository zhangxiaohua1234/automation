#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年06月06日
"""
"""
# 列表的末尾添加元素 .append(x)
list_hogwarts = [1, 2, 3]
list_hogwarts.append(0)
print(list_hogwarts)

# 在指定位置添加元素 .insert(i,x)
list_hogwarts.insert(1, 8)
print(list_hogwarts)

# 移除某个元素
list_hogwarts.remove(8)
print(list_hogwarts)

# 移除指定元素,赋给一个变量之后可以返回出来
y = list_hogwarts.pop(0)
print(list_hogwarts)
print(y)
"""



"""
# sorted()升序排序
list_hogwarts = [1, 5, 3, 7, 2, 6]
list_hogwarts.sort()
print(list_hogwarts)

# sorted()降序排序
list_hogwarts = [1, 5, 3, 7, 2, 6]
list_hogwarts.sort(reverse=True)
print(list_hogwarts)

# 反转列表中的元素
list_hogwarts = [1, 5, 3, 7, 2, 6]
list_hogwarts.reverse()
print(list_hogwarts)
"""


"""
# 列表推导式
# 生成一个平方列表，比如[1,4,9...]使用for循环写
list_square = []
for i in range(1, 4):
    list_square.append(i**2)
print(list_square)

# 使用列表推导式写
list_square2 = [i**2 for i in range(1, 4)]
print(list_square2, "推导式")

# 加入判断条件 if
list_square3 = []
for i in range(1, 4):
    if i != 1:
        list_square3.append(i**2)
print(list_square3)

# 使用列表推导式写
list_square4 = [i**2 for i in range(1, 4) if i != 1]
print(list_square4, "推导式加入if")
"""

# 嵌套循环
list_square5 = []
for i in range(1, 4):
    for j in range(1, 4):
        list_square5.append(i*j)
print(list_square5)

list_square6 = [i*j for i in range(1, 4) for i in range(1, 4)]
print(list_square5, "嵌套循环使用列表推导式写")
