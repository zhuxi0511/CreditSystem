#coding:utf-8

import Tkinter
from Tkinter import Frame, Button, StringVar
from util import Input, Show_style, Password_input, MessageBox
from model import login_model
import const

class Login(Show_style):
    def __init__(self, master=None):
        Show_style.__init__(self, master)
        self.panel_manager = None
        self.user = StringVar()
        self.password = StringVar()
        Frame(master=self,height=100).pack()
        self.create_widget()

    def create_widget(self):
        Input(self, '用户名', self.user).pack(pady=5)
        Password_input(self, '密码', self.password).pack(pady=5)
        self.confirm_button = Button(self, text='确定')
        def login_func(user, password):
            good, user_type = login_model(user, password)
            if good:
                const.user_type = user_type
                const.user_name = self.user.get()
                self.panel_manager.people.status_frame.set_status_text((const.user_name, '客户信息'))
                self.panel_manager.message.status_frame.set_status_text((const.user_name, '消息中心'))
                self.panel_manager.applys.status_frame.set_status_text((const.user_name, '放款申请'))
                self.panel_manager.switch_panel(self, 'message')
            else:
                self.password.set('')
                MessageBox('错误的用户名/密码', '错误的用户名/密码')

        self.confirm_button['command'] = lambda:login_func(self.user.get(), self.password.get())
        self.confirm_button.pack(pady=5)
