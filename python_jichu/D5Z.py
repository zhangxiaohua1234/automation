#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年07月23日
"""
# 5.2 Python 列表的增删改查操作

#1. 列表的添加
# list1 = [1, 2, 3]
# list1.append(666)
# print(list1)
#
# list2 = [1, 2, "a"]
# list2.extend(["java", "python"])
# print(list2)
#
# list3 = [1, 2, "a"]
# list3.insert(0, "张三")
# print(list3)


#2.列表的删除
# list4 = [1, 2, "a"]
# print(list4.pop())
# print(list4.pop(0))
#
#
# list5 = [1, 2, "a"]
# list5.remove("a")
# print(list5)
#
# I = ['老吴', 'test', 'wusir', '龙腾']
# I.clear()
# print(I)
#
# l = ['老吴', 'test', 'wusir', '龙腾']
# del l[0]
# print(l)

# l = ['老吴', 'test', 'wusir', '龙腾']
# del l
# print(l)

# 3.列表的修改：
# l = ['老吴', 'test', 'wusir', '龙腾']
# l[0] = "老张"
# print(l)
#
#
# #4.Python 列表的查找
# l = ['老吴', 'test', 'wusir', '龙腾']
# print("老吴" in l)
#
# if "老吴" in l:
#     l.remove("老吴")
# print(l)


# 5.2.1 列表的排序






# 5.3 Python 元组
# 5.3.2 定义元组
# tup = (11, 22, 33)
# print(type(tup))
#
# tup = ("aa", "bb", 33)
# print(tup[0])
#
# print(tup.index("bb"))
#
# print(tup.count("aa"))
#
# print(len(tup))


# tup1 = ("张三", "李四", "王五")
# del tup1
# print(tup1)


# a = (("刘备", "吕布"), ("老王", "运维"))
# print(a[0])
# print(a[0][1])
# print(a[1][1])


# 5.4 python 字典&集合
# 定义一个字典
# dic = {"name": "Tom", "age": 25}

# 增加
# dic["id"] = "110"
# print(dic)

# 删除
# del dic["age"]
# print(dic)

# 删除整个字典
# del dic
# print(dic)

# dic.clear()
# print(dic)

# 字典的查找
# print(dic["name"])
# print(dic["name1"])

# get查询
# print(dic.get("id"))
# print(dic.get("ida"))

# 查询字典的key和values
# print(dic.keys())

# 返回一个包含字典所有values
# print(dic.values())

# items()
# print(dic.items())


# 5.4.3 字典的循环遍历
# dic = {"name": "Take", "age": 33}
# 遍历字典的key
# for key in dic.keys():
#     print(key)

# 遍历字典的values
# for values in dic.values():
    # print(values)

# 遍历字典元素
# for item in dic.items():
    # print(item)



# 5.5 Python 集合
# 定义一个集合
# set = {1, 2, 3, 4, 4, 4, 5, 5, 6, 3}
# print(type(set))
# print(set)

# 集合的增加
# set.add("Python")
# print(set)

# 集合的删除
# set.remove("Python")
# print(set)
#
# set.pop()
# print(set)
#
# set.clear()
# print(set)