import requests


class TestApi:
    def __init__(self):
        self.session = requests.Session()  # 初始化会话，自动处理Cookie

    def test_login(self):
        # 登录接口（获取有效Cookie）
        login_url = "http://115.28.108.130/newecshop/admin/privilege.php?act=signin"
        login_data = {
            "username": "admin",
            "password": "admin123",
            "act": "signin"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/125.0.0.0 Safari/537.36"
        }
        response = self.session.post(login_url, data=login_data, headers=headers, verify=False)
        if response.status_code != 200:
            raise Exception("登录失败")
        print("登录成功，获取Cookie:", self.session.cookies)

    def test_NewProduct(self):
        # 新增商品接口（自动携带登录后的Cookie）
        url = "http://115.28.108.130/newecshop/admin/goods.php?act=add"

        # 表单数据（注意shop_price需为数字，移除全角字符）
        data = {
            "MAX_FILE_SIZE": "2097152",
            "goods_name": "自动化测试三",
            "cat_id": "360",
            "shop_price": "555",  # 必须为半角数字
            "exclusive": "-1",
            "user_price[]": ["-1", "-1", "-1", "-1"],
            "user_rank[]": ["1", "2", "3", "4"],
            "act": "insert",
            # 其他必填字段...
        }

        # 文件上传（使用会话发送请求）
        files = {
            "goods_img": ("a.png", open(r"D:\python_files\zidonghualianxi\a.png", "rb"), "image/png")
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/125.0.0.0 Safari/537.36",
            "Referer": "http://115.28.108.130/newecshop/admin/goods.php?act=add"
        }

        response = self.session.post(url, data=data, files=files, headers=headers, verify=False)
        print("响应状态码:", response.status_code)
        print("响应内容:", response.text)


if __name__ == "__main__":
    api = TestApi()
    api.test_login()  # 先登录
    api.test_NewProduct()  # 再新增商品
