# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/23
@file: request_handler.py
@function:
@modify:
"""
import requests


class RequestsHandler:
    def __init__(self):
        self.session = requests.Session()

    def visit(self, url, method, params=None, data=None, json=None, headers=None, **kwargs):
        """访问一个接口，你可以是用get请求，也可以是用post请求，put,delete
        请求方法：method
        请求地址：url
        请求参数：params, data, json
        """
        res = self.session.request(method, url, params=params, data=data, json=json, headers=headers,
                                   **kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")

    def clost_session(self):
        self.session.close()