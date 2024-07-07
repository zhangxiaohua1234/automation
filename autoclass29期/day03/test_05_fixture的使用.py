#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月20日
"""
import pytest


@pytest.fixture
def step01():
    print("执行step01")

@pytest.mark.usefixtures("step01")
def test01():
    pass

