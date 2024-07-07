#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月20日
"""
import pytest_check

def test01():
    assert 1+1 == 2
    pytest_check.assert_equal(1+1, 2)
    assert "1" in "123"
    pytest_check.is_in("4", "123", msg="判断是否包含")
    assert ""  is not None
    assert 0 is False
    assert 3 != 5