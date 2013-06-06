#coding:utf-8

import Tkinter
import const
from Tkinter import Frame, Button, LabelFrame, Listbox, Label, StringVar
from util import Input, Show_style, Text_input, MessageBox
from people import PeopleList
from model import save_apply_information
from applysheet import ApplySheetFrame

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
            tmp = self.people_list_frame.get_mutilistbox_choose()
            if not tmp:
                MessageBox('当前用户', '请先选中一个用户')
                return
            people_information, number = tmp
            print people_information
            self.people_list_frame.forget()
            self.apply_information_frame = Apply_information(self)
            self.apply_information_frame.people_name.set(people_information[0])
            self.apply_information_frame.people_number.set(str(1000001+number))
            self.apply_information_frame.number.set(str(100000001+len(const.apply_information_list)))
            self.apply_information_frame.people_information = people_information
            self.apply_information_frame.pack()

        self.people_list_frame = PeopleList(self, title='请选择一个现有客户或录入一个新客户', next_func=apply_func)
        self.people_list_frame['pady'] = 10
        self.people_list_frame.pack()

class Apply_information(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.people_information = None
        self.number = StringVar()
        self.product_name = StringVar()
        self.people_number = StringVar()
        self.people_name = StringVar()
        self.intent = StringVar()
        self.rent_from = StringVar()
        self.aim_to_subject = StringVar()
        self.money_type = StringVar()
        self.money_count = StringVar()
        self.start_date = StringVar()
        self.end_date = StringVar()
        self.limit = StringVar()
        self.rate = StringVar()

        self.fill_application_information()

    def get_information(self):
        print len(self.people_information)
        information_list = []
        information_list.extend(self.people_information)
        information_list.append(self.number.get())
        information_list.append(self.product_name.get())
        information_list.append(self.people_number.get())
        information_list.append(self.people_name.get())
        information_list.append(self.intent.get())
        information_list.append(self.rent_from.get())
        information_list.append(self.aim_to_subject.get())
        information_list.append(self.money_type.get())
        information_list.append(self.money_count.get())
        information_list.append(self.start_date.get())
        information_list.append(self.end_date.get())
        information_list.append(self.limit.get())
        information_list.append(self.rate.get())
        print const.user_type
        information_list.append(str(int(const.user_type) + 1))
        return information_list

    def fill_application_information(self):
        Input(self, '业务编号', self.number).grid(pady=5, row=0, column=0)
        Input(self, '产品名称', self.product_name).grid(pady=5, row=0, column=1)
        Input(self, '客户编号', self.people_number).grid(pady=5, row=1, column=0)
        Input(self, '客户名称', self.people_name).grid(pady=5, row=1, column=1)
        Input(self, '贷款金额', self.money_count).grid(pady=5, row=2, column=0)
        Input(self, '币种', self.money_type).grid(pady=5, row=2, column=1)
        Input(self, '用途说明', self.intent, is_big=True).grid(pady=5, row=3, columnspan=2)
        Input(self, '还款来源', self.rent_from, is_big=True).grid(pady=5, row=4, columnspan=2)
        Input(self, '贷款投向行业', self.aim_to_subject).grid(pady=5, row=5)
        Input(self, '发放日期', self.start_date).grid(pady=5, row=6, column=0)
        Input(self, '到期日期', self.end_date).grid(pady=5, row=6, column=1)
        Input(self, '期限', self.limit).grid(pady=5, row=7, column=0)
        Input(self, '利率', self.rate).grid(pady=5, row=7, column=1)
        self.confirm_button = Button(self, text='确认')
        def confirm_func():
            apply_information = self.get_information()
            self.master.apply_information_frame.forget()
            self.master.apply_confirm_frame = ApplyConfirm(self.master, apply_information)
            self.master.apply_confirm_frame.pack()
        self.confirm_button['command'] = confirm_func
        self.confirm_button.grid(row=8, column=0)
        self.cancel_button= Button(self, text='取消')
        def cancel_func():
            self.master.apply_information_frame.destroy()
            self.master.people_list_frame.pack()
        self.cancel_button['command'] = cancel_func
        self.cancel_button.grid(row=8, column=1)

class ApplyConfirm(Frame):
    def __init__(self, master=None, apply_information=None):
        Frame.__init__(self, master)
        self.apply_information = apply_information
        self.create_widget()
        self.packall()

    def create_widget(self):
        self.title_label = Label(self, text='确定要提交这个申请给上级审核?')
        self.title_label['width'] = 60
        self.apply_sheet_frame = ApplySheetFrame(self, self.apply_information)
        self.confirm_button = Button(self, text='确认')
        def confirm_func():
            if save_apply_information(self.apply_information):
                MessageBox('提交成功', '提交成功, 可以去消息中心查看')
                self.master.apply_confirm_frame.destroy()
                self.master.people_list_frame.pack()
            else:
                MessageBox('提交失败', '出问题拉')
        self.confirm_button['command'] = confirm_func
        self.cancel_button = Button(self, text='取消')
        def cancel_func():
            self.master.apply_confirm_frame.destroy()
            self.master.apply_information_frame.pack()
        self.cancel_button['command'] = cancel_func

    def packall(self):
        self.title_label.grid(pady=5, row=0, column=0, columnspan=2)
        self.apply_sheet_frame.grid(pady=5, row=1, column=0, columnspan=2)
        self.confirm_button.grid(pady=20, row=2, column=0)
        self.cancel_button.grid(pady=20, row=2, column=1)
