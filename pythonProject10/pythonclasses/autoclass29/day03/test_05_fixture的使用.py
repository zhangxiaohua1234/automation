#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年07月11日
"""
import pytest


# @pytest.fixture()
# def setp01(): # 定义一个fixture 函数
#     print('执行step01')
#
#
# def test01(setp01): # 写了一个测试方法，执行test01时，会先执行setp01（把fixture 函数作为用例参数写法，目的是要用函数里的参数）
#     pass


# # -----------------------------------------# @pytest.mark.usefixtures---------------------------
# @pytest.fixture
# def step01():
#     print('执行step01')
#     return 100
#
#
# @pytest.mark.usefixtures('step01')  # 这种写法用不了step01里边的返回值；作用就是在执行test01时先执行了一下step01 函数
# def test01():
#     print(step01)


# # -----------------------------------------# test01 使用 step01 函数中的返回值---------------------------
# @pytest.fixture
# def step01():
#     print('执行step01')
#     return 100
#
#
# def test01(step01):  # 把 step01 传入
#     print(step01)
