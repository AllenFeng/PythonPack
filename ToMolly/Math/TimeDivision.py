# -*- coding: utf-8 -*-
#encoding=utf-8

#V1.0 生成适用于小学二年级的乘法或除法计算题，便于打印

import random,time
from tkinter import *
import tkinter.messagebox

content=[]

def main(max,times,type):
    maxnum = max
    i = 0

    try:
        while i < times:
            var1 = random.randint(0, maxnum)
            var2 = random.randint(0, maxnum)

            if type == 0:   #type =0 进入除法
                result = var1 * var2
                # print('%s / %s = _____ ' % (result, var1))
                fm = '%s / %s = _____ ' % (result, var1)
                print(fm)
                content.append(fm)
                i += 1
            else:           #type=1 进入乘法
                # print('%s * %s = _____ ' % (var1, var2))
                fm = '%s * %s = _____ ' % (var1, var2)
                print(fm)
                content.append(fm)
                i += 1
    finally:
        print(content)

def builddoc():
    randnum = int(time.time())
    doc = open('AL%s.txt'%(randnum),'w')
    m = 1

    for i in content:
        doc.write(i)
        if m % 4 == 0:
            doc.write("\n")
        m += 1

    doc.close()




def getValue():
    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())

    try:
        main(a,b,c)
        builddoc()
        print("已在桌面生成文件")
        info = tkinter.messagebox.showinfo(title='成功', message='生成完成，文件已保存在同文件夹下！')
    except:
        print("生成文件出错")


if __name__ == '__main__':
    root = Tk()
    root.title('小学数学乘除法生成器')
    lb1 = Label(root, text='乘数取值最大范围')
    lb2 = Label(root, text='题目数量')
    lb3 = Label(root, text='题目类型：0=除法，1=乘法')
    entry1 = Entry(root)
    entry2 = Entry(root)
    entry3 = Entry(root)
    btn = Button(root, text='生成试卷', command=getValue)

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)
    lb3.grid(column=0, row=2)

    entry1.grid(column=1, row=0)
    entry2.grid(column=1, row=1)
    entry3.grid(column=1, row=2)

    btn.grid(column=0, row=3)

    root.mainloop()