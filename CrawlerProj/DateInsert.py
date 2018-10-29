#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8


import MySQLdb


# 打开数据库连接
db = MySQLdb.connect("localhost","root","","TEST",charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
#sql = """INSERT INTO DOUBAN_BOOKS(BOOK_NUM,BOOK_NAME,BOOK_VOTE,BOOK_AVG) VALUES (26582558,'电影制作手册（第4版）',20,2.7)"""

sql = """INSERT INTO DOUBAN_BOOKS(BOOK_NUM,
         BOOK_NAME, BOOK_VOTE, BOOK_AVG)
         VALUES (26582558,'电影制作手册（第4版)',20,2.7)"""


try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()