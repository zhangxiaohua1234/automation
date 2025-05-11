#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2025年05月10日
"""
import re

import requests
import jsonpath


class TestApi:
    # 类变量，sess，第六种(有什么区别,需要看底层代码的调用逻辑)
    sess = requests.session()
    # 类变量 token
    token = ""
    csrf_token = ""

    # # 第一个接口，测试登录
    # def test_login(self):
    #     # 请求四要素
    #     method = "get"
    #     url = "https://api.weixin.qq.com/cgi-bin/token"
    #     params = {
    #         "grant_type": "client_credential",
    #         "appid": "wx6b11b3efd1cdc290",
    #         "secret": "106a9c6157c4db5f6029918738f9529d"
    #     }
    #     # 发送请求
    #     res = TestApi.sess.request(method=method, url=url, params=params, verify=False)
    #     # 打印响应数据
    #     result = res.json()
    #     print("第一个接口返回的数据：%s" % result)
    #     #   提取access_token放到token里面
    #     TestApi.token = jsonpath.jsonpath(result, "$.access_token")[0]
    #     # 打印TestApi.token 看下是什么数据类型，是一个列表类型的数据
    #     # print(TestApi.token)
    #
    # # 第二个接口，获取公众号已创建的标签接口
    # def test_select(self):
    #     # 请求四要素
    #     method = "get"
    #     url = "https://api.weixin.qq.com/cgi-bin/tags/get"
    #     params = {
    #         "access_token": TestApi.token
    #     }
    #     # 发送请求
    #     res = TestApi.sess.request(method=method, url=url, params=params, verify=False)
    #     print("第二个接口返回的数据：%s" % res.json())

    # 第三个接口

    def test_start(self):
        # 请求四要素
        method = "get"
        url = "http://47.107.116.139/phpwind/"

        # 发送请求
        res = TestApi.sess.request(method=method, url=url, verify=False)
        result = res.text
        print("第三个接口返回的数据：%s" % result)
        # "<input type="hidden" name="csrf_token" value="edb8c8cdc84bab7a"/>",
        TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"', result).group(1)
        print(TestApi.csrf_token)

    # 第四个接口
    def test_login_phpwind(self):
        # 请求四要素
        method = "post"
        url = "http://47.107.116.139/phpwind/index.php"
        params = {
            "m": "u",
            "c": "login",
            "a": "dorun"
        }

        data = {
            "username": "pytest",
            "password": "pytest",  # 这个密码被老师改了 现在登录不上，所以导致这个case执行不成功的
            "csrf_token": TestApi.csrf_token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {
            "Accept": "application/json,text/javascript,/;q=0.01",
            "X-Requested-With": "XMLHttpRequest",
        }
        # 发送请求
        res = TestApi.sess.request(method=method, url=url, params=params, data=data, headers=headers, verify=False)
        # 打印响应数据
        print("第四个接口返回数据:%s" % res.text)


if __name__ == '__main__':
    ta = TestApi()
    ta.test_login()
    ta.test_select()
    ta.test_start()
    ta.test_login_phpwind()
