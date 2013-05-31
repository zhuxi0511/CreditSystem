#coding:utf-8

import Tkinter
from Tkinter import Frame, Button, LabelFrame, Listbox, Label, Toplevel, StringVar
from util import Input, Text_input, Show_style
from multilistbox import MultiListbox
from model import save_people_information, show_people_list

class People(Show_style):
    def __init__(self, master=None):
        Show_style.__init__(self, master)
        self.add_status()
        self.create_widget()

    def create_widget(self):
        self.people_list_frame = PeopleList(self, title='客户信息表')
        self.people_list_frame.pack(pady=15, ipady=5)

class PeopleList(Frame):
    def __init__(self, master=None, title='', items=(('客户名称',40),('机构类型',10),('国别', 10),('营业执照编号',20),('注册资本',10)), next_func=None):
        Frame.__init__(self, master, relief=Tkinter.GROOVE )
        self.mutilistbox_items = items
        self.next_func = next_func
        self.next_func_button = None
        self.title = title
        self.create_widget()

    def create_widget(self):
        self.create_explain_label()
        self.create_mutilistbox(self.mutilistbox_items)
        self.create_button()
        self.packall()

    def create_explain_label(self):
        self.explain_label = Label(self, text=self.title)
        self.explain_label['width'] = 80
        self.explain_label['anchor'] = 'w'

    def refresh_mutilistbox(self):
        self.people_mutilistbox.delete(0, self.people_mutilistbox.size())
        self.add_item()

    def add_item(self):
        people_list = show_people_list()
        for p in people_list:
            self.people_mutilistbox.insert(Tkinter.END, p)
        
    def create_mutilistbox(self, mutilistbox_items):
        self.people_mutilistbox = MultiListbox(self, mutilistbox_items)
        self.people_mutilistbox['width'] = 200
        self.people_mutilistbox['height'] = 100
        self.refresh_mutilistbox()

    #TODO
    def create_button(self):
        self.add_people_button = Button(self, text='增加新客户')
        self.add_people_button['command'] = lambda: PeopleInformationToplevel(self)
        self.confirm_button = Button(self, text='刷新')
        self.confirm_button['command'] = self.refresh_mutilistbox
        if self.next_func:
            self.next_func_button = Button(self, text='填写申请')
            self.next_func_button['command'] = self.next_func

    def packall(self):
        self.explain_label.pack()
        self.people_mutilistbox.pack(fill=Tkinter.BOTH)
        self.confirm_button.pack(side=Tkinter.RIGHT)
        self.add_people_button.pack(side=Tkinter.RIGHT)
        if self.next_func_button:
            self.next_func_button.pack(side=Tkinter.LEFT)

class PeopleInformationToplevel(Toplevel):
    def __init__(self, father, title='添加客户信息'):
        Toplevel.__init__(self)
        self.name = StringVar()
        self.people_type = StringVar()
        self.nation = StringVar()
        self.org_code = StringVar()
        self.check_data = StringVar()
        self.cride_code = StringVar()
        self.signed_data = StringVar()
        self.company_type = StringVar()
        self.company_address = StringVar()
        self.money_type = StringVar()
        self.money_count = StringVar()
        self.company_range = StringVar()
        self.tex_code = StringVar()
        self.tex_type = StringVar()
        self.tex_data = StringVar()
        self.father = father
        self.title(title)
        self.create_widget()
        self.pack_all()

    def get_information(self):
        information_list = []
        information_list.append(self.name.get())
        information_list.append(self.people_type.get())
        information_list.append(self.nation.get())
        information_list.append(self.org_code.get())
        information_list.append(self.check_data.get())
        information_list.append(self.cride_code.get())
        information_list.append(self.signed_data.get())
        information_list.append(self.company_type.get())
        information_list.append(self.company_address.get())
        information_list.append(self.money_type.get())
        information_list.append(self.money_count.get())
        information_list.append(self.company_range.get())
        information_list.append(self.tex_code.get())
        information_list.append(self.tex_type.get())
        information_list.append(self.tex_data.get())
        return map(lambda x:x.strip(), information_list)

    def create_widget(self):
        self.name_input = Input(self, '客户名称', self.name)
        self.name_input.entry['width'] = 60
        self.company_type_input = Input(self, '公司类型', self.company_type)
        self.company_type_input.entry['width'] = 60
        self.company_address_input = Input(self, '注册地址', self.company_address)
        self.company_address_input.entry['width'] = 60
        self.confirm_button = Button(self, text='确定')
        def confirm_button_func():
            save_people_information(self.get_information())
            self.father.refresh_mutilistbox()
            self.destroy()
        self.confirm_button['command'] = confirm_button_func
        self.cancel_button = Button(self, text='取消')
        self.cancel_button['command'] = self.destroy

    def pack_all(self):
        Label(self, text='添加客户信息').grid(row=0, pady=20, columnspan=3 )
        self.name_input.grid(row=1, pady=5, column=0, columnspan=2)
        Label(self, width=10).grid(row=1, column=2)
        Input(self, '机构类型', self.people_type).grid(row=2, pady=5, column=0)
        Input(self, '国别', self.nation).grid(row=2, pady=5, column=1)
        Label(self, text='机构代码信息', anchor='w', width=35).grid(row=3, column=0, pady=10)
        Input(self, '组织机构代码', self.org_code).grid(row=4, pady=5, column=0)
        Input(self, '年检到期日', self.check_data).grid(row=4, pady=5, column=1)
        Label(self, text='注册信息', anchor='w', width=35).grid(row=5, column=0, pady=10)
        Input(self, '营业执照编号', self.cride_code).grid(row=6, pady=5, column=0)
        Input(self, '注册登记日', self.signed_data).grid(row=6, pady=5, column=1)
        self.company_type_input.grid(row=7, pady=5, column=0, columnspan=2)
        self.company_address_input.grid(row=8, pady=5, column=0, columnspan=2)
        Input(self, '注册本金币种', self.money_type).grid(row=9, pady=5, column=0)
        Input(self, '注册资本', self.money_count).grid(row=9, pady=5, column=1)
        Text_input(self, '经营范围', self.company_range).grid(row=10, pady=5, column=0, columnspan=2)
        Label(self, text='税务信息', anchor='w', width=35).grid(row=11, column=0, pady=10)
        Input(self, '税务登记证件类型', self.tex_type).grid(row=12, pady=5, column=0)
        Input(self, '税务登记证号', self.tex_code).grid(row=12, pady=5, column=1)
        Input(self, '年检到期日', self.tex_data).grid(row=13, pady=5, column=0)
        self.confirm_button.grid(row=14, column=0, pady=10)
        self.cancel_button.grid(row=14, column=1)

