#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("New.txt", "a")
print "文件名: ", fo.name

# 对文件写值
fo.write( "gogogo");

# 关闭一个文件
fo.close()