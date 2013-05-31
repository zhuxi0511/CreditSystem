#coding:utf-8

import Tkinter
from Tkinter import Frame, Button, LabelFrame, Listbox, Label, StringVar
from util import Input, Show_style, Text_input
from people import PeopleList

class Apply(Show_style):
    def __init__(self, master=None):
        Show_style.__init__(self, master)
        self.add_status()
        self.create_sidebar()
        self.create_widget()

    def create_sidebar(self):
        self.sidebar_frame = Frame(self)
        self.sidebar_frame['relief'] = 'groove'
        self.sidebar_frame['borderwidth'] = 2
        self.choose_people_sidebar_label = Label(self.sidebar_frame, text='选择客户')
        self.choose_people_sidebar_label['width'] = 20 
        self.fill_apply_sidebar_label = Label(self.sidebar_frame, text='填写申请')
        self.submit_sidebar_label = Label(self.sidebar_frame, text='提交申请')
        self.choose_people_sidebar_label.pack(fill=Tkinter.X)
        self.fill_apply_sidebar_label.pack(fill=Tkinter.X)
        self.submit_sidebar_label.pack(fill=Tkinter.X)
        Label(self.sidebar_frame, height=1000).pack(fill=Tkinter.BOTH)

        self.sidebar_frame['pady'] = 20
        self.sidebar_frame.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

    def create_widget(self):
        def apply_func():
            self.people_list_frame.forget()
            self.apply_information_frame = Apply_information(self)
            self.apply_information_frame.pack()

        self.people_list_frame = PeopleList(self, title='请选择一个现有客户或录入一个新客户', apply_func)
        self.people_list_frame['pady'] = 10
        self.people_list_frame.pack()

class Apply_information(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.number = StringVar()
        self.product_name = StringVar()
        self.people_number = StringVar()
        self.people_name = StringVar()
        self.intent = StringVar()
        self.intent_explain = StringVar()
        self.rent_from = StringVar()
        self.aim_to_subject = StringVar()
        self.money_type = StringVar()
        self.date = StringVar()

        self.fill_application_information()

    def fill_application_information(self):
        Input(self, '业务编号', self.number).grid(pady=5, row=0, column=0)
        Input(self, '产品名称', self.product_name).grid(pady=5, row=0, column=1)
        Input(self, '客户编号', self.people_number).grid(pady=5, row=1, column=0)
        Input(self, '客户名称', self.people_name).grid(pady=5, row=1, column=1)
        Input(self, '借款用途', self.intent).grid(pady=5, row=2)
        Text_input(self, '借款用途说明', self.intent_explain).grid(pady=5, row=3, columnspan=3)
        Text_input(self, '还款来源', self.rent_from).grid(pady=5, row=4, columnspan=2)
        Input(self, '贷款投向行业', self.aim_to_subject).grid(pady=5, row=5)
        Input(self, '币种', self.money_type).grid(pady=5, row=6, column=1)
        Input(self, '日期', self.date).grid(pady=5, row=6, column=0)
        self.confirm_button = Button(self, text='确认')
        self.confirm_button.grid(columnspan=2)
