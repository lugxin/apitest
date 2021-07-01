# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/25
@file: run_test.py
@function:
@modify:
"""
import os
import time
import unittest

from config.setting import config
from libs.HTMLTestRunner_cn2 import HTMLTestRunner


# 加载器
testloader = unittest.TestLoader()
suite = testloader.discover(config.case_path)

# 通过模块名，类名

# 测试报告格式
ts = str(int(time.time()))
file_name = 'test_result_{}.html'.format(ts)
file_path = os.path.join(config.report_path, file_name)

with open(file_path, 'wb') as f:
    runner = HTMLTestRunner(f,
                            title='接口测试报告',
                            description='接口测试报告',
                            tester='LongNight')
    runner.run(suite)