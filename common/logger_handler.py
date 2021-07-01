# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/25
@file: mylogging.py
@function:
@modify:
"""
"""
封装log方法
"""

import logging


class LoggerHandler(logging.Logger):

    def __init__(self, name='root', level='DEBUG', file=None,
                 format='[%(filename)s]:[%(lineno)d]:[%(name)s]:[%(levelname)s-%(message)s'):
        super().__init__(name)

        # 设置级别
        self.setLevel(level)

        fmt = logging.Formatter(format)

        # 初始化处理器
        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        stream_handler = logging.StreamHandler()

        # 设置 handler 的级别
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


if __name__ == '__main__':
    logger = LoggerHandler(file='demo.txt')
    logger.error('hello world!')
