#coding:utf-8

import Tkinter
from Tkinter import Button, LabelFrame, Listbox
from util import Input, Show_style

class Message(Show_style):
    def __init__(self, master=None):
        Show_style.__init__(self, master)
        self.add_status()
        self.create_widget()

    def create_widget(self):
        self.main_labelframe = LabelFrame(self, text='消息中心')
        self.main_list = Listbox(self.main_labelframe, height=22, width=100)
        self.main_list['selectmode']=Tkinter.BROWSE
        self.main_list.pack(padx=10, pady=10)
        self.main_list.insert(1,'asdfa')
        self.main_list.insert(234,'234')
        def printList(event):
            print self.main_list.curselection()
        self.main_list.bind('<Double-Button-1>',printList) 
        self.main_labelframe.pack()

        #TODO confirm command function
        self.confirm_button = Button(self.main_labelframe, text='察看')
        self.confirm_button['command'] = None
        self.confirm_button.pack()
        self.confirm_button = Button(self.main_labelframe, text='')
