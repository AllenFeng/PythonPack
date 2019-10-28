# -*- coding: utf-8 -*-

import random
import time
import sys
from operator import add, sub

count = 0
right = 0

while True:

    a = random.randint(2, 3)
    list = []

    for i in range(a):
        list.append(random.randint(1,10))

    op = ['+', '-']
    d = random.choice(op)
    d2 = random.choice(op)


    if d == '+':
        answer = list[0] + list[1]
    else:
        answer = list[0] - list[1]
    questionContent=str(list[0])+str(d)+str(list[1])+"="


    if a == 3:
        if d2 == '+':
            answer = answer + list[2]
        else:
            answer = answer - list[2]
        questionContent=str(list[0])+str(d)+str(list[1])+str(d2)+str(list[2])+"="

    print('准备出题了...')
    time.sleep(1)
    print(questionContent)
    userAnswer = input('请输入正确答案： (按q退出)')

    if userAnswer == str(answer):
        print('回答正确')
        count += 1
        right += 1
    elif userAnswer == 'q':
        break
    else:
        print('回答错误')
        count += 1

percent = right / count
print('测试结束,共回答%d道题,正确个数为%d,正确率为%.2f%%' % (count, right, percent * 100))


