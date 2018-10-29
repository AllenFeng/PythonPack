#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

r_url = 'http://api.map.baidu.com/geocoder/v2/?address=中潭路100弄330号&output=json&ak=BC5433370064e80211497ec8d30b1bd2&callback=showLocation'

r=requests.get(r_url)

print r.text