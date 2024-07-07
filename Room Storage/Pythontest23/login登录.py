import unittest
from selenium import webdriver
from time import sleep

class logincase(unittest.TestCase):
    def setUp(self):
        self.dr=webdriver.Firefox()
        self.dr.get("http://115.28.108.130/zentaopms/www/index.php?m=user&f=login")
        print("111")
    def test01(self):
        sleep(2)
        self.dr.find_element_by_id("account").send_keys("admin")
        self.dr.find_element_by_name("password").send_keys("123456")
        self.dr.find_element_by_id("submit").click()
        sleep(4)
        print(self.dr.switch_to.alert.text)
        self.assertEqual("登录失败，请检查您的用户名或密码是否填写正确。", self.dr.switch_to.alert.text)
        print("我是test01")

    def test02(self):
        self.dr.find_element_by_id("account").send_keys("")
        self.dr.find_element_by_name("password").send_keys("123456")
        self.dr.find_element_by_id("submit").click()
        sleep(4)
        print(self.dr.switch_to.alert.text)
        self.assertEqual("登录失败，请检查您的用户名或密码是否填写正确。", self.dr.switch_to.alert.text)
        print("我是test02")

    def tearDown(self):
        self.dr.quit()
        print(222)
if __name__ == '__main__':
    unittest.main()
