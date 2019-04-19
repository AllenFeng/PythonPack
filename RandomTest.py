# -*- coding: UTF-8 -*-
# 目的：测试在超级大量的次数后，骰子的6个面出现的概率是基本一致的

import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
allcnt = 0

for order in range(100000):
    a = random.randint(1,6)
    if a == 1 :
        one = one +1
    elif a == 2:
        two = two + 1
    elif a == 3:
        three = three +1
    elif a == 4:
        four = four + 1
    elif a == 5:
        five = five + 1
    else:
        six = six + 1
    allcnt = allcnt + 1


print '总共统计了',allcnt,'次'
print '1的出现概率=',round(one/float(allcnt),4)
print '2的出现概率=',round(two/float(allcnt),4)
print '3的出现概率=',round(three/float(allcnt),4)
print '4的出现概率=',round(four/float(allcnt),4)
print '5的出现概率=',round(five/float(allcnt),4)
print '6的出现概率=',round(six/float(allcnt),4)