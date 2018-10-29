#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 用途:批量修改iphone目录下的照片,然后合并至小米路由器内
# V1.0.0
# create at 2017-09-22


import os,time,datetime

path='/Users/Allen/downloads/私人文档/rename_test'
i=0
files = os.listdir(path)

for filename in files:
    portion=os.path.splitext(filename)

    a=path+'/'+filename
    t=os.path.getctime(a)
    tt=datetime.datetime.fromtimestamp(t)
    filetimepart = tt.strftime('%Y%m%d')

    newname=filetimepart + str(i) + portion[1]
    i=+1
    os.rename(path+'/'+filename,path+'/'+newname)
    print(os.path.basename(filename)+' -> '+os.path.basename(newname))