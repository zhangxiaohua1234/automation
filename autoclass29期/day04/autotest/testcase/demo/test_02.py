#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月27日
"""
import pytest
import logging
# logging.info()
# logging.debug()
# logging.error()
# logging.warning()

@pytest.mark.smoke
def test_02():
    logging.info("执行test")
    pass


def test_c():
    pass


def test_d():
    pass