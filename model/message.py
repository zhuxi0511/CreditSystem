#coding:utf-8

import Tkinter
import const
from copy import deepcopy
from Tkinter import Button, LabelFrame, Listbox, Toplevel, Label
from util import Input, Show_style, MessageBox
from multilistbox import MultiListbox
from model import show_apply_list, save_apply_information
from applysheet import ApplySheetFrame

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
        self.main_list_item = (('业务编号',10),('客户编号',8),('客户名称',20),('发放日',10),('到期日',10),('贷款金额',5),('产品名称',10),('期限', 5),('利率',8), ('申请状态', 14))
        self.main_list = MultiListbox(self.main_labelframe, self.main_list_item, height=22)
        self.main_list.grid(padx=10, pady=10, row=0, column=0)

        self.check_button = Button(self.main_labelframe, text='察看')
        def check_func():
            apply_information = self.get_mutilistbox_choose()
            if not apply_information:
                MessageBox('当前申请', '请先选中一个申请消息')
                return
            self.apply_information_toplevel = ApplyInformationToplevel(self, apply_information)
        self.check_button['command'] = check_func
        self.check_button.grid(pady=10, row=1, column=0)
    
    def get_mutilistbox_choose(self):
        now = self.main_list.curselection()
        if not now:
            return None
        else:
            print 'now', self.main_list.get(now)
            number = self.main_list.get(now)[0]
            #return const.apply_information_list[int(now[0])]
            for apply_information in const.apply_information_list:
                if apply_information[15] == number:
                    return apply_information

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
            elif now_state < int(const.user_type):
                continue
            self.main_list.insert(Tkinter.END, p)

    def pack_all(self):
        self.main_labelframe.pack()

class ApplyInformationToplevel(Toplevel):
    def __init__(self, master, apply_information, title='申请业务详情'):
        print 'apply_information', apply_information
        Toplevel.__init__(self)
        self.master = master
        self.apply_information = apply_information
        self.title(title)
        self.create_widget()
        self.pack_all()

    def create_widget(self):
        self.apply_state_label = Label(self, text='当前申请状态:%s' % self.get_state(), fg='red')
        self.apply_sheet_frame = ApplySheetFrame(self, self.apply_information)
        self.submit_apply_button = None
        if (int(const.user_type) < 4):
            self.submit_apply_button = Button(self, text='通过并提交上级审核')
        else:
            self.submit_apply_button = Button(self, text='通过审核')
        self.submit_apply_button['state'] = 'disable'
        def submit_apply_func():
            tmp = deepcopy(self.apply_information)
            tmp[-1] = str(int(self.apply_information[-1])+1)
            const.apply_information_list.remove(self.apply_information)
            save_apply_information(tmp)
            self.master.refresh_mutilistbox()
            self.destroy()
        self.submit_apply_button['command'] = submit_apply_func
        self.confirm_button = Button(self, text='确认')
        self.confirm_button['command'] = self.destroy
        self.print_apply_sheet = Button(self, text='打印借据')
        self.print_apply_sheet['state'] = 'disable'

    def pack_all(self):
        self.apply_state_label.grid(pady=20, row=0, column=0, columnspan=3)
        self.apply_sheet_frame.grid(pady=5, padx=20, row=1, column=0, columnspan=3)
        self.submit_apply_button.grid(pady=5, row=2, column=0)
        self.confirm_button.grid(pady=10, row=2, column=1)
        self.print_apply_sheet.grid(pady=10, row=2, column=2)
        if '等待当前用户审核' == self.get_state():
            self.submit_apply_button['state'] = 'normal'
        if '审核通过' == self.get_state():
            self.print_apply_sheet['state'] = 'normal'

    def get_state(self):
        ret = None
        now_state = int(self.apply_information[-1])
        if now_state >= 5:
            ret = '审核通过'
        elif now_state > int(const.user_type):
            ret = '等待上级审核'
        elif now_state == int(const.user_type):
            ret = '等待当前用户审核'
        return ret
