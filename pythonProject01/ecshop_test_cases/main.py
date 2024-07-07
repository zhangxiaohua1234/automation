#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2024年05月29日
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/15 14:49
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

import os

# 这是程序入口
if __name__ == "__main__":
    os.system("pytest")

'''
通过 pytest ...命令,可以实现非常灵活的执行控制，常用的参数如下：详细显示模式：-v，否则执行通过的用例只显示一个点；
安静模式：-q：不显示环境信息；
显示跳过、期望失败、非期望成功的用例：-rxX
命令行显示 print 输出：-s，否则捕获用例输出并显示到报告中；运行目录及子包下的所有用例：pytest 目录名；
运行指定模块所有用例：pytest test_reg.py
运行指定模块指定类指定用例：pytest test_reg.py::TestClass::test_method
运行名称包含指定表达式的用例：-k 表达式(支持 and or not),如pytest -k "test_a andtest_b" 运行指定标签(mark)的用例： -m 标签(支持 and or not), 如 pytest -m "apitest and level1" 遇到失败后停止：-x/--exitfirst 首次失败后退出(可用于保留出错现场) --maxfail=3 3 次失败后退出
执行上次失败的用例 --lf/--last-failed
先执行上次失败的用例,再执行成功的用例 --ff/--failed-first
只收集用例，不执行 --collect-only
显示执行最慢的前 N 条用例：--durations=N
显示所有可用的 Fixture 函数：--fixtures
'''
