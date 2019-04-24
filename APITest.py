# -*- coding: UTF-8 -*-

import requests

import requests
url = "http://sandbox.duitku.com/webapi/api/merchant/v2/inquiry"
headers = {'content-type': 'application/json'}
requestData = {"name": "lance", "age": "28"}
ret = requests.post(url, json=requestData, headers=headers)
if ret.status_code == 200:
    text = json.loads(ret.text)
    print(text)