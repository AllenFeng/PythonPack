#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8


import MySQLdb

class DataInsert:

    def __init__(self):
        pass


    def execute(cls,pagenum,name,vote,avg):
        # 打开数据库连接
        db = MySQLdb.connect("localhost","root","","TEST",charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = "INSERT INTO DOUBAN_BOOKS(BOOK_NUM,BOOK_NAME, BOOK_VOTE, BOOK_AVG) VALUES (%s,'%s',%s,%s)" % (pagenum,name,vote,avg)


        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except :
           # Rollback in case there is any error
           db.rollback()

        # 关闭数据库连接
        db.close()
