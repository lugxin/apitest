# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/27
@file: test_login.py
@function:
@modify:
"""
import json
import unittest

import yaml

from apiframework.common.db_handler import DBHandler
from apiframework.common.excel_handler import ExcelHandler
from apiframework.common.helper import generate_mobile
from apiframework.common.logger_handler import LoggerHandler
from apiframework.common.request_handler import RequestsHandler
from apiframework.common.yaml_handler import yaml_data
from apiframework.config.setting import config
from apiframework.libs import ddt


# yaml 读取
# f = open(config.yaml_config_path, encoding='utf-8')
# yaml_data = yaml.load(f, Loader=yaml.FullLoader)
# print(yaml_data)

@ddt.ddt
class TestLogin(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('login')  # excel中的用例表单名称

    logger = LoggerHandler(name=yaml_data['logger']['name'],
                           level=yaml_data['logger']['level'],
                           file=yaml_data['logger']['file'])

    def setUp(self):
        self.req = RequestsHandler()

        self.db = DBHandler(host=yaml_data['database']['host'],
                            port=yaml_data['database']['port'],
                            user=yaml_data['database']['user'],
                            password=yaml_data['database']['password'],
                            database=yaml_data['database']['database'],
                            charset=yaml_data['database']['charset'])

    def tearDown(self) -> None:
        self.req.clost_session()
        self.db.close()

    @ddt.data(*data)
    def test_login(self, test_data):
        pass
