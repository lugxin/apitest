# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/27
@file: yaml_handler.py
@function:
@modify:
"""
import yaml

from apiframework.config.setting import config


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read(self, encoding='utf-8'):
        # yaml 读取
        f = open(self.file, encoding=encoding)
        # TODO:f.read() 和 f 都可以作为参数
        data = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
        return data


# 读取本项目当中的yaml配置项
yaml_data = YamlHandler(config.yaml_config_path).read()
