#第一百七十一节 python讲解第一天
# print ("hello world")
# jsondata="pm.response.json()"#把后边的值赋给jsondata，下次想再使用"pm.response.json()时，直接用变量jsondata替代就行了，方便下次使用
# print(jsondata) #print 是一个输出的函数

                         #第一百七十二节 python第一天02  运算符使用+-*/% // == true false and  or 使用方法
# a=14#  a==14#判a是不是等于14
# b=0
# c=1

# a=-b  #把-b赋值给a
# a=+b  #把+b赋值给a
# a-=b  #a=a-b
# a+=b  #a=a+b
# a%=b#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)   返回除法的余数
# print(a//b)  返回商的整数部分
# print(a==15)  判断a是不是等于15；答案是true/false

# print(a and b) #两个数中有假数时，输出假数
# print(b and a) #两个数中有假数时，输出假数
# print(a or b)  #两个数中有假数时，输出真数
# print(b or a)  #两个数中有假数时，输出真数
# print(a and c) #两个数都为真数时，输出右边的真数
# print(c and a) #两个数都为真数时，输出右边的真数
# print(a or c)   #两个数都为真数时，输出左边的真数
# print(c or a)  #两个数都为真数时，输出左边的真数
#print（c and a or c） 输出a
# a=15  重新定义a，那么上边的a=14就做废了


                                               # 基本数据类型、查看数据类型、
# a=[2,"dbc",[1,4]]  #列表
# b={
#     "code": "1",
#     "msg": "登录成功",
#     "data": {
#         "key": "eec7897f5714d938e5cc5bbd4a3386d6",
#         "userid": "16213",
#         "data": "eec7897f5714d938e5cc5bbd4a3386d6",
#         "expiry": "tingting e10adc3949ba59abbe56e057f20f883e1631933811",
#         "time": 1631933811
#     }
# } #字典---服务端的接口
# print(b["data"]["key"]) #取字典型里边的值
# print(a[2][0])  #取列表里的值
# c=1 #整型
# d="abcasddf" #字符串型
# f=1.333 #浮点型
# e="123" #字符串型  只要是在引号里边就是字符串类型，单引号与双引号一样
# print(type(a),type(b),type(c),type(d),type(f),type(e))  #查看ABCDEF字段类型的函数
# #<class 'list'> <class 'dict'> <class 'int'> <class 'str'> <class 'float'>  list列表  dict字典 int整型  str字符串 folat浮点型
# print("//n")  #/n是换行符
# print("1234")


#字符串截取 方法
# print(d[0]) #取字符串的字符 读取到第0个是a
# print(d[1:4]) #读取1到4区间的数 bca
# print(d[-1]) #取倒数第一个  负数为-1为开始数，正数以0为开始数
#
# print(len(a),len(b),len(d),len(b["data"])) #输出长度，只适合打印、字典、列表、字符串类型；不能打印整型和浮点型





                                  #20210323“python字符窜常用方法”   成员运算符 in 使用方法
#1、判断字符串是否在另一个串中
# d="abcasddf64614sfefaaf" #字符串型
# # print("a" in d) #变量d中是否包含字符a
# 变量d中包含字符a，就显示pass
# # if ("a" in d):
# #     print("pass")
# 字符串相加是 拼接
# d="abdfdfsad"
# c="1234"
# print(d+c)
# 整数相加是 计算
# f=1
# e=2
# print(f+e)


# 内置函数len 使用方法   在使用函数的使用用的是();在提取值的时候使用的是[]
# print(len(d)) #取整个字符串的长度
# print(d[-1]) #取最后一个字符串
# #通过正数的顺序+结合长度
# print(d[len(d)-1])  整个字符串长度减1和这个print(d[-1])得到的结果是一样的
# print(len(d)/2) #得到字符串数量/2  得到的是 浮点数
# print(d[len(d)//2-2]) #商取整数，得到的是某一个字符串




                                       # #“python之基本逻辑结构”
#把小写英文字符串d转换成大写
# d="abdfdfsad"
# print(d.upper())
#查找字符串中字符的序号位置
# print(d.find("f"))

# input()使用方法；是用于接收键盘的输入的方法；将输入的值转化为字符串
# c=input("请输入：")
# print(c)
# print(type(c)) #查看是否为字符串类型




                             # #第一百九十三节 “python常用的逻辑结构”input()输入使用方法
# c=input("请输入：")
# d=int(c) #把字符串c转换成int整型
# print(type(c),type(d))
# len,print,type,input,int  常用函数





                                 #第一百九十四节 “python的逻辑结构02”  if条件与while循坏
# if语法，条件使用方法
# if 0:
#     print(13242)
# else:
#     print("我是对的")    #if 如果为真就执行if；如果if为假就运行else

#如果a=b，则输出相等，否则输出不相等
# a=int(input("请输入"))# 是用于接收键盘的输入的方法；将输入的值转化为字符串
# b=1
# if a==b:
#     print("相等")
# else:
#     print("不相等")

#从键盘输入一个数字，假如大于b输出及格，否则输出不及格
# a=input("请输入")
# a=int(a)
# b=60
# if a>=b:
#     print("及格")
# else:
#     print("不及格")

# 从键盘输入一个数字，假如在0到60分，输出不及格
# 假如在60-90分之间输出良好，在90-100之间输出优秀，否则输出超出范围
# a=int(input("请输入"))
# b=60
# c=90
# if 0<=a<=60:
#     print("不及格")
# elif 60<a<=90:
#     print("良好")
# elif 90<a<=100:
#     print("优秀")
# else :
#     print("超出范围")

                                               # while循环方法使用
# 输出1到10之内的数字
# n = 1
# while n < 11:
#     print(n)
#     n = n+1





                                           # python之for循环及练习讲解
#接上节：用while输出100包含100以内的偶数
# 方法一:使用比较固定
# n = 0
# while n <= 100:
#     print(n)
#     n = n+2
# 方法二：方法比较活 因为n改变为任何值公式输出的都是偶数
# n=0
# while n<=100:
#     if n%2==0:
#         print(n)
#     n=n+1

# #取出100以内的奇数、偶数和
# n=100
# sum1=0
# sum=0
# while n>0:
#     if n%2==0:
#         sum1+=n
#     else:
#         sum=sum+n
#     n-=1
# print(sum1,sum)

# 作业：使用while循环计算 100以内的偶数之和
# 方法一：
# sum=0
# n=100
# while n>0:
#     sum+=n   #sum+n如果和n-=2 调换位置，那么结果为2450；因为是先做了减法在进行计算的
#     n -= 2
# print(sum)
# 方法二：
# sum=0
# n=100
# while n>0:
#     if n%2==0:
#         sum+=n
#     n=n-1
# print(sum)

#使用if判断；输入一个数字，判断平年还是闰年；能被4整除不能被100整除或者能被400整除的是润年；其它是平年
# a=int(input("请输入"))
# if (a%400==0) or (a%4==0 and a%100!=0):   运算优先级从左到右，不加括号也可以
#     print("闰年")
# else:
#     print("平年")






                                 # 第一百九十六节 “for循环”
# for循环使用方法
# names = "xyzab"
# n=1
# for name in names:  #查看变量name是不是在names循环体里，name可以自定义
#     print(name)   #循环体names里有多少值就循环几次
#     n=n+1
# print(n)

# range范围；使用方法
#range(10)=[0,1,2,3,4,5,6,7,8,9]   做可视化，不能运行

# 使用range和for循环、if条件计算100以内的奇数和、偶数和
# n=range(101)
# s=0
# sum=0
# for a in n:
#     if a%2==0:
#         sum+=a
#     else:
#         s=s+a
# print(sum,s)







                                     # 第二百一十八节 20210929“python之列表，字典的基本方法”
# append 使用方法 列表末尾插入
# d=[1,2,3,4,5,6,4]
# d.append("abc")
# print(d)
# # insert根据指定位置插入
# d.insert(4,int(565665))
# print(d)
# d.insert(4,"xyz")
# print(d)
#求某一个值的第一个匹配项的位置
# d.index("xyz")
# d.remove("abc")#删除指定的值
# d.remove("xyz")
# d.sort()#从小到大排序
# print(d)
# d.reverse()#反转列表中的元素
# 例题2
# d=[6,9,7,5,8,5]
# d.sort()
# print(d)
# d.reverse()
# print(d)

# list1使用方法
# list1=[5,3,1,7]
# # 求低于这个列表的最小整数
# list1.sort()
# print(list1[0]-1)


#使用if判断；输入一个数字，判断平年还是闰年；能被4整除不能被100整除或者能被400整除的是润年；其它是平年
# a=int(input("请输入"))
# if (a%400==0) or (a%4==0 and a%100!=0):   运算优先级从左到右，不加括号也可以
#     print("闰年")
# else:
#     print("平年")

# list2=[]
# n=range(0,2001)
# for i in n:
#     if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
#        list2.append(i)
# print(list2)

# 定义创建空字典
# dict1={}
# # 向空字典里插入数据
# dict1["age"]=1
# dict1["abc"]="165456"
# print(dict1)
# # 求字典中有几段数
# print(len(dict1))
# # 取字典的值
# print(dict1["abc"]) #方法1
# print(dict1.get("abc"))  #方法2
# print(dict1)
# print(len(dict1["abc"]))

# b={
#     "code": "1",
#     "msg": "登录成功",
#     "data": {
#         "key": "eec7897f5714d938e5cc5bbd4a3386d6",
#         "userid": "16213",
#         "data": "eec7897f5714d938e5cc5bbd4a3386d6",
#         "expiry": "tingting e10adc3949ba59abbe56e057f20f883e1631933811",
#         "time": 1631933811
#     }
# }
# print(b["data"]["key"])  #取出来b中data中key的值
# for i in  b:
#     print(i)  #取出key的值
#     print(b[i])  #去除所有的value
#
# dict2={"name":"sddfsdsf","tel":23465423,"sex":"女"}
# 求这个字典中有没有value的为longteng，如果没有，就打印没有
# list1=[{"name":"huxiaoyan","tel":"156"},{"name":"wangyang","tel":"137"},{"name":"huxiaoyan1","tel":"123"}]
# # 判断该字典中是否有姓名为”huxiaoyan”,如果有，则取出对应的电话号码，否则打印该姓名不存在。
# flag=0
# for i in list1:
#     if i["name"]=="huxiaoyan":
#         print(i["tel"])
#         flag=1
# if flag==0:
#     print("不存在")
#


# 函数
# def ffd(x):
#     print(x)

# print(ffd("holou"))


# def abc(x,y):
#     z=x+y
#     print(z)
#     return z
# print(abc(4,5))
#
# def ffd(a):
#     if a%2==0:
#         return "偶数"
#     else:
#         return "奇数"
# print(ffd(51))
#
#
# def abc(x):
#     a = 0
#     for z in range(x+1):
#         a=a+z
#     return a
# print(abc(9))
#
#

# “导包”
# 类
class father:
    def __init__(self,name,face,nose,age):  #init初始化
        self.name=name
        self.face=face
        self.nose=nose
        self.age=age
    def getattr(self):
       return self.age

p=father("long","small","high",18)
print(p.getattr())

class son(father):
    def __init__(self,sex,max,age):
        self.sex=sex
        self.max=max
        self.age=age
s=son("teng","big",19)
print(s.getattr())