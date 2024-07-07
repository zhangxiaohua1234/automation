#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月27日
"""
import json
import logging
import conftest

from conftest import BASE_DIR
import json, yaml, toml

class JSON_UTILS:
    #加载json文件
    def json_file_load(self, file_path):
        logging.info("加载json文件："+str(file_path))
        with open(file_path, 'r',  encoding="utf-8") as f:
            return json.load(f)


    #加载json字符串
    def json_str_load(self, json_str):
        return json.loads(json_str)

    #字典转json文件
    def dict_to_json_file(self, dict, file_path):
        with open(file=file_path, mode="w", encoding="utf-8") as f:
            json.dump(lbj=dict, fp=file_path)


    #字典转字符串
    # def dict_to_json_str(self, dict):
    #     return json.dump()


# class YAML_UTILS:
#     def load_yaml(self, file_path, encoding='utf-8'):
#         """à© yml HI£°X±²³ß®)Äëí PyYAML"""
#         logging.debug('加载yaml文件: %s' % file_path)
#         with open(file_path, 'r', encoding=encoding) as f:
#             return yaml.safe_load(f)
#
#         def load_toml(self, file_path, encoding='utf-8'):
#             """à© toml HI£°X±²³ß®)Äëí TOML"""
#
#         logging.debug('加载yaml文件: %s' % file_path)
#         with open(file_path, 'r', encoding=encoding) as f:
#             return toml.load(f)
# ym = YAML_UTILS().load_yaml()(BASE_DIR.TESTDATA_DIR / "demo.yaml")
# print(ym)
# class CsvTool:
#     pass