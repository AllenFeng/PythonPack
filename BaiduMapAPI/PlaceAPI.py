#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

s_url = 'http://api.map.baidu.com/place/v2/search?query=银行&location=39.915,116.404&radius=2000&output=json&ak=BC5433370064e80211497ec8d30b1bd2'

r=requests.get(s_url)

print r.json()
