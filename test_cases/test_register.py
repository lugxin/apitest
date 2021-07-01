# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/25
@file: test_register.py
@function:
@modify:
"""
import json
import os
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
class TestRegister(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('login')  # excel中的用例表单名称

    logger = LoggerHandler(name=yaml_data['logger']['name'],
                           level=yaml_data['logger']['level'],
                           file=os.path.join(config.log_path, yaml_data['logger']['file']))

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
    def test_register(self, test_data):
        # 访问接口，得到实际结果
        print(test_data)
        # 判断 test_data['json']如果出现了#exist_phone#,使用generate_mobile
        # 随机生成一个手机号码替换 #exist_phone#
        # if '#exist_phone#' in test_data['data']:
        #     # mobile = generate_mobile()
        #     # 查询数据库，如果数据库当中存在该手机号码，那么我们直接使用这个号码
        #     mobile = self.db.query('select * from account;')
        #     if mobile:
        #         # 直接查询数据库，随机找一个，直接使用该号码替换
        #         # 替换#exist_phone#
        #         test_data['data'] = test_data['data'].replace("#exost_phone#", mobile['mobile_phone'])
        #     else:
        #         # 随机生成一个手机号码
        #         # 注册成功,通过接口注册，直接通过插入数据库
        #         pass
        # if '#new_phone#' in test_data['data']:
        #     while True:
        #         gen_mobile = generate_mobile()
        #         # 查询数据库，如果数据库当中存在该手机号码，那么我们再生成一次，直到不存在为止
        #         mobile = self.db.query('select * from account where account_id=%s;', args=[gen_mobile])
        #         # 直接查询数据库，随机找一个，直接使用该号码替换
        #         # 替换#exist_phone#
        #         if not mobile:
        #             break
        #     test_data['data'] = test_data['data'].replace("#exist_phone#", gen_mobile)

        # 访问接口，得到实际结果，字符串
        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['data']),
                             headers=json.loads(test_data['headers']))
        try:
            # 获取预期结果
            self.assertEqual(test_data['expected'], res['message'])
            # 写入 excel 数据
            self.excel_handler.write(config.data_path,
                                     'login',
                                     test_data['case_id'] + 1,
                                     9,
                                     '测试通过')
        except AssertionError as e:
            # 记录 logger
            self.logger.error("测试用例失败:{}".format(e))
            # 手动抛出异常，否则测试用例会自动通过
            self.excel_handler.write(config.data_path,
                                     'login',
                                     test_data['case_id'] + 1,
                                     9,
                                     '测试失败')
            raise e

    # 如果出现断言失败，要将失败的用例记录到 logger 当中

    # 把实际结果写入excel 文档
