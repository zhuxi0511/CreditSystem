#coding:utf-8

import Tkinter
from Tkinter import Frame, Button, StringVar
from util import Input, Show_style, Password_input

class Login(Show_style):
    def __init__(self, master=None):
        Show_style.__init__(self, master)
        self.user = StringVar()
        self.password = StringVar()
        Frame(master=self,height=100).pack()
        self.create_widget()

    def create_widget(self):
        """
        self.user_entry = Entry(self, textvariable=self.user)
        self.password_entry = Entry(self, textvariable=self.password)
        self.password_entry['show'] = '*'
        self.confirm_button = Button(self, text='确定')
        self.confirm_button['command'] = None
        self.user_entry.pack()
        self.password_entry.pack()
        self.confirm_button.pack()
        """
        Input(self, '用户名', self.user).pack(pady=5)
        Password_input(self, '密码', self.password).pack(pady=5)
        #TODO confirm command function
        self.confirm_button = Button(self, text='确定')
        self.confirm_button['command'] = None
        self.confirm_button.pack(pady=5)
