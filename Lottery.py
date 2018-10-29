#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
root = Tk()

class LotteryWindow(Frame):
	
	levelcount = '0'
	
	def __init__(self):
		lab1 = Label(root, text="请输入总楼层")
		lab1.pack()

		ent1 = Entry(root)
		ent1.pack()

		btn1 = Button(root, text="抽奖",command = self.btnclick)
		btn1.pack()

		lab2 = Label(root, font=16)
		lab2.pack()	
		
		root.mainloop()	


	def btnclick():
			
		levelcount = ent1.get()
		print("输入的数字为: ",levelcount)
		
		return
		
if __name__ == '__main__':
	LotteryWindow().mainloop()










