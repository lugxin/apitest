# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/25
@file: setting.py
@function:
@modify:
"""
import os


class Config:
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path, 'data/demo.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path, 'test_cases')

    # config路径
    config_path = os.path.join(root_path, 'config')

    # 测试报告路径
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    # log路径
    log_path = os.path.join(root_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    # yaml路径
    yaml_config_path = os.path.join(config_path, 'config.yaml')


class DevConfig(Config):
    # 项目的域名
    host = 'http://119.147.171.113:8070'


config = DevConfig()
