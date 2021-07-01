# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:LongNight
@time: 2021/03/26
@file: demo_pymysql.py
@function:
@modify:
"""
import pymysql

# 建立连接
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='119.147.171.113', port=13306,
                       user='zhidian', password='zdsh123',
                       charset='utf8', database='mall_csmc',
                       cursorclass=DictCursor)

# 游标，数据库操作当中一个重要的概念。
cursor = conn.cursor()

# 执行sql语句
cursor.execute('SELECT * FROM ACCOUNT')

# 得到结果
one = cursor.fetchone()
all = cursor.fetchall()

print(one)

cursor.close()
conn.close()
