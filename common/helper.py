# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/26
@file: helper.py
@function:
@modify:
"""
import random
import re

from common.request_handler import RequestsHandler
from common.yaml_handler import yaml_data
from config.setting import config
from jsonpath import jsonpath


def generate_mobile():
    """随机生成一个手机号码1[3,5,7,8,9] + 9"""
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for i in range(9):
        num = random.randint(0, 9)
        phone += str(num)
    return phone


class Context:
    member_id = None
    token = ''


def login():
    """登录，返回的是token和member_id
    1.从登录的excel当中读取
    2.从配置文件当中读取
    """
    req = RequestsHandler()
    res = req.visit(config.host + '/login',
                    'post',
                    json=yaml_data['user'],
                    headers={"": " "})
    return res


def save_token():
    # 保存token信息
    data = login()
    token = jsonpath(data, '$..token')[0]
    member_id = jsonpath(data, '$..token')[0]
    Context.token = token
    Context.member_id = member_id
    return token


def replace_label(target):
    """while循环"""
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern, target):
        # 如果能够匹配
        key = re.search(re_pattern, target).group(1)
        # Content.token
        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target


if __name__ == '__main__':
    data = save_token()
    print(generate_mobile())
    print(data)
