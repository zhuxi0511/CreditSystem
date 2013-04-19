#coding:utf-8

import Tkinter
from Tkinter import Frame, Entry, Label, Button, Text

class Input(Frame):
    def __init__(self, master=None, text='', textvariable=None):
        Frame.__init__(self, master)
        self.text = text
        self.textvariable = textvariable
        self.create_widget()

    def create_widget(self):
        self.create_text(self.text)
        self.create_entry(self.textvariable)
        self.pack_all()

    def create_text(self, text):
        self.text_label = Label(self, text=text)
        self.text_label['width'] = 16
        self.text_label['anchor'] = 'e'

    def create_entry(self, textvariable):
        self.entry = Entry(self, textvariable=textvariable)

    def pack_all(self):
        self.text_label.pack(side=Tkinter.LEFT)
        self.entry.pack()

class Text_input(Input):
    def __init__(self, master=None, text='', textvariable=None):
        Input.__init__(self, master, text, textvariable)

    def create_entry(self, textvariable):
        self.entry = Text(self)
        self.entry['height'] = 5
        self.entry['width'] = 60 
        self.text_label['height'] = 5
        self.text_label['anchor'] = 'ne'

class Password_input(Input):
    def __init__(self, master=None, text='', textvariable=None):
        Input.__init__(self, master, text, textvariable)
        self.entry['show'] = '*'

class Show_style(Frame):
    def __init__(self, master=None, text='对公信贷系统'):
        Frame.__init__(self, master)
        self.title_label = Label(self, text=text, height=3, width=100, bg='grey')
        self.title_label['font'] = 'Helvetica -32'
        self.title_label.pack()

    def add_status(self):
        self.status_frame = Status(self)
        self.status_frame['relief'] = 'groove'
        self.status_frame['borderwidth'] = 2
        self.status_frame.pack(fill=Tkinter.BOTH)

class Status(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.create_widget()

    def create_widget(self):
        self.create_message_button()
        self.create_apply_button()
        self.create_people_button()
        self.create_status_text()
        self.pack_all()

    def create_message_button(self):
        self.message_button = Button(self, text='消息中心')
        self.message_button['command'] = None

    def create_apply_button(self):
        self.apply_button = Button(self, text='放款申请')
        self.apply_button['command'] = None
        
    def create_people_button(self):
        self.people_button= Button(self, text='客户信息')
        self.people_button['command'] = None
        
    def create_status_text(self):
        self.status_text_label = Label(self, text='当前用户> 当前>', width=80)
        self.status_text_label['anchor'] = 'e'

    def pack_all(self):
        self.message_button.pack(side=Tkinter.LEFT)
        self.apply_button.pack(side=Tkinter.LEFT)
        self.people_button.pack(side=Tkinter.LEFT)
        self.status_text_label.pack()

