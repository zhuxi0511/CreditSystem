#coding:utf-8

import Tkinter
from Tkinter import Frame, Button, LabelFrame, Listbox, Label
from util import Input, Show_style
from multilistbox import MultiListbox

class People(Show_style):
    def __init__(self, master=None):
        Show_style.__init__(self, master)
        self.add_status()
        self.create_widget()

    def create_widget(self):
        self.people_list_frame = People_list(self, title='客户信息表')
        self.people_list_frame.pack(pady=15, ipady=5)

class People_list(Frame):
    def __init__(self, master=None, title='', items=(('col1',10),('col2',10),('col3',60)) ):
        Frame.__init__(self, master, relief=Tkinter.GROOVE )
        self.mutilistbox_items = items
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

    #TODO
    def add_item(self):
        self.people_mutilistbox.insert(Tkinter.END, (1, 2, 3))
        self.people_mutilistbox.insert(Tkinter.END, (1, 2, 3))
        
    def create_mutilistbox(self, mutilistbox_items):
        self.people_mutilistbox = MultiListbox(self, mutilistbox_items)
        self.people_mutilistbox['width'] = 200
        self.people_mutilistbox['height'] = 100
        self.add_item()

    def create_button(self):
        self.add_people_button = Button(self, text='增加新客户')
        self.confirm_button = Button(self, text='查看')

    def packall(self):
        self.explain_label.pack()
        self.people_mutilistbox.pack(fill=Tkinter.BOTH)
        self.confirm_button.pack(side=Tkinter.RIGHT)
        self.add_people_button.pack(side=Tkinter.RIGHT)
