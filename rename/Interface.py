#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self, master)
        self.place(height=200,width=1000)
        self.createWidgets()

    def createWidgets(self):
        #渲染控件
        self.sourceLab = tk.Label(self,text="source fold")
        self.openButton = tk.Button(self, text='Open',command=self.quit)

        self.targetLab = tk.Label(self,text="target fold")
        self.open2Button = tk.Button(self, text='Open',command=self.quit)

        self.execButton = tk.Button(self, text='Open',command=self.quit)

        #显示控件
        self.sourceLab.grid()
        self.openButton.grid()
        self.targetLab.grid()
        self.open2Button.grid()
        self.execButton.grid()


app = Application()
app.master.title('Sample application')
app.mainloop()