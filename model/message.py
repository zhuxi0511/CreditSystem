#coding:utf-8

import Tkinter
import const
from Tkinter import Button, LabelFrame, Listbox
from util import Input, Show_style
from multilistbox import MultiListbox
from model import show_apply_list

class Message(Show_style):
    def __init__(self, master=None):
        Show_style.__init__(self, master)
        self.add_status()
        self.create_widget()
        self.pack_all()

    def create_widget(self):
        self.create_main_frame()

    def create_main_frame(self):
        self.main_labelframe = LabelFrame(self, text='消息中心')
        self.main_list_item = (('业务编号',10),('客户编号',10),('客户名称',25),('发放日',10),('到期日',10),('贷款金额',5),('产品名称',10),('期限', 5),('利率',10), ('申请状态', 16))
        self.main_list = MultiListbox(self.main_labelframe, self.main_list_item, height=22)
        """
        def printList(event):
            print self.main_list.curselection()
        self.main_list.bind('<Double-Button-1>',printList) 
        self.main_list.grid(padx=10, pady=10, row=0, column=0, columnspan=4)
        """

        #TODO confirm command function
        self.check_button = Button(self.main_labelframe, text='察看')
        self.check_button['command'] = None
        self.check_button.grid(pady=10, row=1, column=1)
        """
        self.submit_apply_button = None
        if (const.user_type < 4):
            self.submit_apply_button = Button(self.main_labelframe, text='通过并提交上级审核')
        else:
            self.submit_apply_button = Button(self.main_labelframe, text='通过审核')
        self.submit_apply_button.grid(pady=10, row=1, column=2)
        """

    def refresh_mutilistbox(self):
        self.main_list.delete(0, self.main_list.size())
        self.add_item()

    def add_item(self):
        apply_list = show_apply_list()
        for p in apply_list:
            now_state = int(p[-1])
            if now_state >= 5:
                p[-1] = '审核通过'
            elif now_state > int(const.user_type):
                p[-1] = '等待上级审核'
            elif now_state == int(const.user_type):
                p[-1] = '等待当前用户审核'
            self.main_list.insert(Tkinter.END, p)

    def pack_all(self):
        self.main_labelframe.pack()

