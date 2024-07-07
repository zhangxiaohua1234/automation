#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月20日
"""
import pytest

x = 10
@pytest.fixture(scope="module", autouse=True)
def setp01():
    global x
    x = 20
    print("模块启动")


@pytest.fixture(scope="session", autouse=True)
def setp02():
    global x
    x = 5
    print("会话启动")


@pytest.fixture(scope="package", autouse=True)
def setp03():
    global x
    x = 50
    print("包（目录）启动")


@pytest.fixture(scope="class", autouse=True)
def setp04():
    global x
    x += 80
    print("类启动")


def test_01(setp01):
    print("执行测试用例01", x)


class Test01:

    def setup_method(self):
        global x
        x += 80

    def test01(self):
        print(x+10)

    def test02(self):
        print(x+20)

#跟老师的答案不一致，下来再看看