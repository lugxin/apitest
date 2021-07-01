# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/27
@file: test_recharge.py
@function:
@modify:
"""
import json
import unittest

import yaml

from apiframework.common.db_handler import DBHandler
from apiframework.common.excel_handler import ExcelHandler
from apiframework.common.helper import save_token, Context
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
class TestRecharge(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('recharge')  # excel中的用例表单名称

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
        # 登录
        # 获取结果
        save_token()  # 访问登录接口，得到token值

    def tearDown(self) -> None:
        self.req.clost_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        """充值接口"""
        # 1.替换json数据当中的member_id ,#member_id# 替换成Context.member_id
        # 2.访问接口，得到实际结果
        # 3.断言实际结果是否==预期结果
        token = Context.token
        member_id = Context.member_id
        if "#member_id#" in test_data['data']:
            test_data['data'] = test_data['data'].replace("#member_id#", str(member_id))

        if "*wrong_member*" in test_data['data']:
            test_data['data'] = test_data['data'].replace("*wrong_member*", str(member_id))
        # 读取excel当中的headers，得到字典
        headers = json.loads(test_data['headers'])
        # 添加token
        headers['Authorization'] = token
        # 访问接口，得到实际结果，字符串
        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['data']),
                             headers=headers)

        # 断言
        self.assertEqual(res['code'], test_data['expected'])

        for k, v in json.loads(test_data['expected']).items():
            # msg,code
            if k in res:
                self.assertEqual(res[k], v)
        # 断言是否成功用例，如果是成功用例，校验数据库
        if res['code'] == '0':
            # 查看数据库结果，充值金额+充值之前的金额 == 充值之后的金额
            money = json.loads(test_data['data'])['account']
            # 获取充值之前的余额
            # 获取充值之后的余额
