#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年07月12日
"""
import pytest


# conftest 是集中管理fixture 的文件
@pytest.fixture
def step01():
    print('执行step01，conftest')
    return 100
