#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年07月10日
"""
import pytest

# @pytest.fixture(scope='module')
# def setp01():
#     print('模块启动')
#
# def test_01(setp01): # 把setp01传入到test_01方法中，然后就先执行 setp01 ，再执行test_01
#     print('执行测试用例01')

x = 10


# # -----------------------------------autouse=True 的作用 和 test_01中调用setp01 里的global参数----------------------
# @pytest.fixture(scope='module',
#                 autouse=True)  # autouse = True 的作用是 def test_01(): 方法括号里不用传 setp01 就可以直接执行。输出‘模块启动’
#                 ，只是一个初始化；但test_01()里边调用不到里边的变量（global x
# # x = 20）:
# def setp01():
#     global x
#     x = 20
#     print('模块启动')
#
#
# def test_01():
#     print('执行测试用例01', x)


# # ----------------------------------test_01中传入 setp01 的方式，需要再estp01 中写return x进行 返回----------------------
# @pytest.fixture(scope='module', autouse=True)
# # x = 20）:
# def setp01():
#     global x
#     x = 20
#     print('模块启动')
#     return x
#
#
# def test_01(setp01):
#     print('执行测试用例01', x)


# # ----------------------------------会话、模块、类、方法启动的优先级顺序----------------------
# @pytest.fixture(scope='module', autouse=True)
# # x = 20）:
# def setp01():
#     global x
#     x = 20
#     print('模块启动')
#     return x
#
#
# @pytest.fixture(scope='session', autouse=True)
# # x = 20）:
# def setp02():
#     global x
#     x = 5
#     print('会话启动')
#     return x
#
#
# @pytest.fixture(scope='package', autouse=True)
# # x = 20）:
# def setp03():
#     global x
#     x = 50
#     print('包启动')
#     return x
#
#
# @pytest.fixture(scope='class', autouse=True)
# # x = 20）:
# def setp04():
#     global x
#     x = 80
#     print('类启动')
#     return x
#
#
# def test_01(setp01):
#     print('执行测试用例01', x)


# # ----------------------------------会话、模块、类、方法启动的优先级顺序及计算---这里讲的有点问题，每次执行下边返回的数据不一样--
@pytest.fixture(scope='module', autouse=True)
# x = 20）:
def setp01():
    global x
    x = 20
    print('模块启动')
    return x


@pytest.fixture(scope='session', autouse=True)
# x = 20）:
def setp02():
    global x
    x = 5
    print('会话启动')
    return x


@pytest.fixture(scope='package', autouse=True)
# x = 20）:
def setp03():
    global x
    x = 50
    print('包启动')
    return x


@pytest.fixture(scope='class', autouse=True)
# x = 20）:
def setp04():
    global x
    x += 80
    print('类启动')
    return x


def test_01(setp01):
    print('执行测试用例01', x)


class Test01:
    def setup_method(self):
        global x
        x += 80

    def test01(self):
        print(x + 10)

    def test02(self):
        print(x + 20)
