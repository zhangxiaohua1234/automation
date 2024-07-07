import unittest
from login登录 import logincase
from register import  MyTestCase
import register
import htmlrunner
s=unittest.TestSuite() #TestSuite 实例化了类，传属性后，转成对象s
s.addTest(logincase("test01"))
s.addTest(MyTestCase("test02"))
fp=open("D:\软件测试题\\report.html",'wb')
runner=htmlrunner.HTMLTestRunner(fp,title='我是')
runner.run(s)
fp.close()