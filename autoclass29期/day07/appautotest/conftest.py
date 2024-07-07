#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年08月27日
"""
import os

import pytest
from datetime import datetime

from pathlib import Path
from selenium import webdriver
from utils import send_email_utils


class BASE_DIR():
    PROJECT_DIR = Path(__file__).parent  # print(PROJECT_DIR)
    TESTDATA_DIR = PROJECT_DIR / "data"
    TESTLOGS_DIR = PROJECT_DIR / "logs"
    PAGE_DIR = PROJECT_DIR / "page"
    REPORT_DIR = PROJECT_DIR / "report"
    REPORT_DATA_DIR = REPORT_DIR / "report_data"
    REPORT_HTML_DIR = REPORT_DIR / "report_html"
    TESTCASE_DIR = PROJECT_DIR / "testcase"
    UTILS_DIR = PROJECT_DIR / "UTILS"


@pytest.fixture
def driver():
    driver = webdriver.Remote("http://127.0.0.1:4723")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addini('send_email', help="")
    parser.addini('gen_report', help="")


def pytest_configure(config):
    log_file_name = config.getini("log_file")  # ---> logs/test.log
    now = datetime.now()
    if log_file_name:
        config.option.log_file = config.rootdir / now.strftime("logs/%Y年/%m月/%d日/%H%M%S.log")

    if config.getini("gen_report"):
        config.option.allure_report_dir = BASE_DIR.REPORT_DATA_DIR


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if config.getini("gen_report"):
        os.system(f"allure generate {BASE_DIR.REPORT_DATA_DIR}"
                  f" -o {BASE_DIR.REPORT_HTML_DIR} --clean")
    if config.getini("send_email"):
        # ini = config.ini
        # sender = config.ini("sender")
        # passwd = config.ini("passwd")
        # host = config.ini("host")
        # accpet = config.ini("accpet")
        # accpet = accpet.split(',')
        # subject = config.ini("subject")
        # context = config.ini("context")
        # attach = config.ini("attach")
        # cc = config.ini("cc").split(',')
        # 3660298953

        sender = "1281038043@qq.com"
        passwd = "arsnkssnnlmofjah"
        host = "smtp.qq.com"
        accpet = "3660298953@qq.com"
        subject = "xxxcshibaogao"
        context = "hi, all"
        attach = "./ report / report_html"
        cc = "3660298953@qq.com"
        email = send_email_utils.SEND_EMAIL(sender, passwd, host, accpet, subject, context, attach, cc)
        email.send()
