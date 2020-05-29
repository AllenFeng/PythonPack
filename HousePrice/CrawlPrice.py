# -*- coding: utf-8 -*-
#encoding=utf-8

import time
import requests
import pandas as pd
from pyquery import PyQuery as pq


currentURL="https://sh.lianjia.com/xiaoqu/5011000003476/"
myUrl = currentURL
headers = { 'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'text/html; charset=utf-8'}

r = requests.get(currentURL,headers=headers)
doc = pq(r.text)

avgPrice = doc('span[class=xiaoquUnitPrice]').text()
xiaoqu = doc('h1[class=detailTitle]').text()
address = doc('div[class=detailDesc]').text()
recorddata=time.strftime('%Y-%m-%d',time.localtime(time.time()))
recordtime=time.strftime('%H:%M:%S',time.localtime(time.time()))

dataframe = pd.DataFrame({'小区名':xiaoqu, '地址':address, '均价':avgPrice, '创建日期':recorddata, '创建时间':recordtime},index=[0])
dataframe.to_csv("ods_houseprice.csv",mode='a',header=False,index=True,sep=',')




print(xiaoqu)
print(address)
print(avgPrice)
print(recorddata)
print(recordtime)