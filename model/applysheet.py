#coding:utf-8

import Tkinter
import const
from Tkinter import Frame, Label

class ApplySheetFrame(Frame):
    def __init__(self, master=None, apply_information=None):
        Frame.__init__(self, master)
        self.apply_information = apply_information
        self.create_widget()
        self.pack_all()

    def create_widget(self):
        pass

    def pack_all(self):
        Label(self, text='业务编号', relief='groove', borderwidth=1, width=12).grid(row=0, column=0, columnspan=2)
        Label(self, text=self.apply_information[15], relief='groove', borderwidth=1, width=40).grid(row=0, column=2)
        Label(self, text='产品名称', relief='groove', borderwidth=1, width=10).grid(row=0, column=3, columnspan=2)
        Label(self, text=self.apply_information[16], relief='groove', borderwidth=1, width=40).grid(row=0, column=5)
        Label(self, text='借款人', relief='groove', borderwidth=1, width=8, height=2).grid(row=1, column=0, rowspan=2)
        Label(self, text='名称', relief='groove', borderwidth=1).grid(row=1, column=1)
        Label(self, text=self.apply_information[18], relief='groove', borderwidth=1, width=40).grid(row=1, column=2)
        Label(self, text='编号', relief='groove', borderwidth=1).grid(row=2, column=1)
        Label(self, text=self.apply_information[17], relief='groove', borderwidth=1, width=40).grid(row=2, column=2)
        Label(self, text='借款用途', relief='groove', borderwidth=1, width=10, height=2).grid(row=1, column=3, rowspan=2, columnspan=2)
        Label(self, text=self.apply_information[19], relief='groove', borderwidth=1, width=40, height=2).grid(row=1, column=5, rowspan=2)
        Label(self, text='利率', relief='groove', borderwidth=1, width=8).grid(row=4, column=0)
        Label(self, text=self.apply_information[27], relief='groove', borderwidth=1, width=44).grid(row=4, column=1, columnspan=2)
        Label(self, text='借款发放日', relief='groove', borderwidth=1, width=10).grid(row=4, column=3, columnspan=2)
        Label(self, text=self.apply_information[24], relief='groove', borderwidth=1, width=40).grid(row=4, column=5)

        Label(self, text='期限', relief='groove', borderwidth=1, width=8).grid(row=5, column=0)
        Label(self, text=self.apply_information[26], relief='groove', borderwidth=1, width=44).grid(row=5, column=1, columnspan=2)
        Label(self, text='借款到期日', relief='groove', borderwidth=1, width=10).grid(row=5, column=3, columnspan=2)
        Label(self, text=self.apply_information[25], relief='groove', borderwidth=1, width=40).grid(row=5, column=5)
        Label(self, text='借款金额', relief='groove', borderwidth=1, width=8).grid(row=6, column=0)
        Label(self, text='币种', relief='groove', borderwidth=1).grid(row=6, column=1)
        Label(self, text=self.apply_information[22], relief='groove', borderwidth=1, width=40).grid(row=6, column=2)
        Label(self, text='金额(大写)', relief='groove', borderwidth=1, width=10).grid(row=6, column=3, columnspan=2)
        Label(self, text=self.apply_information[23], relief='groove', borderwidth=1, width=40).grid(row=6, column=5)
        Label(self, text='本人同意将上述借款转入收款人账户\n\n借款人签章', anchor='nw', relief='groove', borderwidth=1, width=52, height=6).grid(row=7, column=0, columnspan=3)
        Label(self, text='银行签章\n\n信贷部门主管\n\n信贷员', anchor='nw', relief='groove', borderwidth=1, width=50, height=6).grid(row=7, column=3, columnspan=3)
