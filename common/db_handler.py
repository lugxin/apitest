# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/26
@file: db_handler.py
@function:
@modify:
"""
import pymysql
import yaml
from pymysql.cursors import DictCursor

from apiframework.config.setting import config


class DBHandler:
    def __init__(self, host, port,
                 user, password,
                 charset, database=None,
                 cursorclass=DictCursor, **kwargs):
        """初始化"""
        self.conn = pymysql.connect(host=host, port=port,
                                    user=user, password=password,
                                    charset=charset, database=database,
                                    cursorclass=cursorclass, **kwargs)
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, one=True):
        """查询语句"""
        self.cursor.execute(sql, args=args)
        # TODO:提交事务
        self.conn.commit()
        # 获取结果
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        """关闭连接"""
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # 参数读取yaml配置文件
    f = open(config.yaml_config_path, encoding='utf-8')
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    print(yaml_data)
    db = DBHandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   database=yaml_data['database']['database'],
                   charset=yaml_data['database']['charset'])
    res = db.query("select * from account;")
    print(res)