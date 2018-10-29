#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests,json,pprint


geo_url= 'http://api.map.baidu.com/geocoder/v2/?address=中潭路100弄330号&output=json&ak=BC5433370064e80211497ec8d30b1bd2'

g=requests.get(geo_url)
new_g=json.load(g.json().read())

print new_g