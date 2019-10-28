# -*- coding: utf-8 -*-

# FT means Feature
#Version 0.5

import urllib.request as req
import re
import json
import jsonpath

url = 'https://www.zhihu.com/people/xu-feng-57/following?page=1'


webContent = req.urlopen(url)

contentData = webContent.read()
contentData = contentData.decode('utf-8')

#1. 个人基本信息
#1.1 昵称
nickName = re.search('(?<=<span class="ProfileHeader-name">)(.*)(?=</span><span class="ztext ProfileHeader-headline">)',contentData, re.M)
#1.2 行业
industry = re.search('(?<=</g></svg></div>)(.*)(?=</div><div class="ProfileHeader-infoItem">)', contentData, re.M)

#2. 个人成就信息
#2.1 获得赞同

#2.2 获得感谢

#3. 关注信息
#3.1 关注了
followingAllContent = re.findall('(?<=<script id="js-initialData" type="text/json">)(.*)(?<="subAppName":"main"})', contentData, re.M)
print(type(followingAllContent))
print(followingAllContent)

fo = json.load(followingAllContent)

print(fo)


#3.2 关注者


