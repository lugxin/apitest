# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/28
@file: demo_reg.py
@function:
@modify:
"""
import re


class Context:
    token = ''
    username = 'lgx'


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
    mystr = '{"memeber_id": "#member_id#"}'
    re_pattern = r'#(.*?)#'
    a = replace_label(mystr)
    print(a)
