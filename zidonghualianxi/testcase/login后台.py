#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2025年05月11日
"""
# ---------------------------------------------------------------------------------商城后台-登录
import requests


class TestApi:
    cookie = ""

    def test_login(self):
        # 商城后台-登录
        url = 'http://115.28.108.130/newecshop/admin/privilege.php'

        url_params = {
            "username": "admin",
            "password": "admin123",
            "act": "signin",
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "ECS_LastCheckOrder=Wed%2C%2014%20May%202025%2014%3A00%3A52%20GMT",
        }
        res = requests.post(url, data=url_params, headers=headers, verify=False)
        info = [
            res.text,
            res.url,
            res.headers,
            res.cookies,
            res.request.headers
        ]
        for i in info:
            print(i, end='\n')

        result = res.request.headers
        TestApi.cookie = result.get("Cookie")
        print("打印cookie %s" % TestApi.cookie)

    def test_NewProduct(self):
        # 商城后台-新增商品
        import requests

        url = "http://115.28.108.130/newecshop/admin/goods.php?act=add"

        headers = {
            "Cookie": TestApi.cookie,
        }

        # 处理表单数据（包含文件上传）
        # 处理表单数据（包含文件上传）
        files = {
            "goods_img": ("a.png", open(r"D:\python_files\zidonghualianxi\a.png", "rb"), "image/png")
        }

        data = {
            "MAX_FILE_SIZE": "209715",
            "goods_name": "自动化测试四",  # 注意：原curl中的乱码已修正为正确中文
            "goods_sn": "",
            "cat_name": "运动户外",
            "cat_id": "360",
            "addedCategoryName": "",
            "other_cat[]": "0",
            "brand_search": "请输入……",
            "brand_search_bf": "",
            "brand_search_jt": "",
            "addedBrandName": "",
            "brand_id": "0",
            "brand_name": "",
            "suppliers_id": "0",
            "shop_price": "555",  # 注意：原curl中的全角数字已修正为半角
            "exclusive": "-1",
            "user_price[]": ["-1", "-1", "-1", "-1"],
            "user_rank[]": ["1", "2", "3", "4"],
            "volume_number[]": "",
            "volume_price[]": "",
            "market_price": "NaN",
            "give_integral": "-1",
            "rank_integral": "-1",
            "buymax_start_date": "",
            "buymax_end_date": "",
            "cost_price": "0",
            "goods_img_url": "商品图片外部URL",
            "auto_thumb": "1",
            "goods_desc": "",
            "goods_weight": "",
            "weight_unit": "1",
            "goods_number": "1",
            "warn_number": "1",
            "ghost_count": "",
            "is_on_sale": "1",
            "is_alone_sale": "1",
            "keywords": "",
            "goods_brief": "",
            "seller_note": "",
            "goods_type": "0",
            "cat_id1": "360",
            "brand_id1": "0",
            "keyword1": "",
            "is_single": "1",
            "cat_id2": "360",
            "brand_id2": "0",
            "keyword2": "",
            "price2": "",
            "article_title": "",
            "goods_id": "0",
            "act": "insert"
        }

        # 发送POST请求（自动处理multipart/form-data边界）
        response = requests.post(url, headers=headers, data=data, files=files, verify=False)

        # 打印响应结果
        print("响应状态码:", response.status_code)
        print("响应内容:", response.text)

# def test_list(self):
#     # 商城后台-管理中心商品列表查询
#     url = 'http://115.28.108.130/newecshop/admin/goods.php?act=ajax_category'
#
#     headers = {
#         "Cookie": TestApi.cookie,
#     }
#     res = requests.post(url, headers=headers, verify=False)
#
#     info = [
#         res.json(),
#     ]
#     for i in info:
#         print(i, end='\n')


if __name__ == '__main__':
    TestApi().testlogin()

