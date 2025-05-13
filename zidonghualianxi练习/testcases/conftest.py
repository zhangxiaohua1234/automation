#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2025年05月12日
"""
import pytest


@pytest.fixture(scope="session", autouse=False)
def exe_sql():
    print("链接数据库")
    yield "success"
    print("关闭数据库的链接")
