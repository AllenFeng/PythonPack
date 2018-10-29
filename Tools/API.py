#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode

#----------------------------------
# 影讯API合集调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/42
#----------------------------------

def main():

    #配置您申请的APPKey
    appkey = "33598b97dad849ebfd6cf7b0cb053f5c"

    #1.按关键字检索影片信息
    request1(appkey,"GET")


#按关键字检索影片信息
def request1(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/index"
    params = {
        "title" : "你的名字", #需要检索的影片标题,utf8编码的urlencode
        "smode" : "", #&lt;font color=red&gt;是否精确查找，精确:1 模糊:0  默认1&lt;/font&gt;
        "pagesize" : "", #&lt;font color=red&gt;每次返回条数，默认20,最大50&lt;/font&gt;
        "offset" : "", #&lt;font color=red&gt;偏移量，默认0,最大760&lt;/font&gt;
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml/json，默认json
    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#临时性代码,将接收到的数据写入a.txt
    f=open('a.txt','w')
    f.write(content)
    f.closed


if __name__ == '__main__':
    main()