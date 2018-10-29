# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import thread
import time

currentURL="http://www.cninfo.com.cn/information/financialreport/szmb000651.html"
myUrl = currentURL

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent,
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'text/html; charset=GB2312'}

req = urllib2.Request(myUrl, headers = headers)
myResponse = urllib2.urlopen(req)
myPage = myResponse.read()
print myPage