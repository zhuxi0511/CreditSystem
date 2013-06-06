#coding:utf-8

import Tkinter
from Tkinter import Frame, Entry, Label, Button, Text, Toplevel
import const

class MessageBox(Toplevel):
    def __init__(self, title='', message=''):
        Toplevel.__init__(self)
        self.title(title)
        self.message = message
        self.create_widget()
        self.pack_all()

    def create_widget(self):
        self.message_label = Label(self, text=self.message)
        self.message_label['width'] = 40 
        self.message_label['anchor'] = 'center'
        self.message_label['wraplength'] = 200
        self.message_label['justify'] = 'left'
        self.ok_button = Button(self, text='确定')
        self.ok_button['command'] = self.destroy

    def pack_all(self):
        self.message_label.grid(pady=20, row=0)
        self.ok_button.grid(pady=5, row=1)

class Input(Frame):
    def __init__(self, master=None, text='', textvariable=None, is_big=False):
        Frame.__init__(self, master)
        self.text = text
        self.is_big = is_big
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
        if self.is_big:
            self.entry['width'] = 60 

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
        self.panel_manager = None
        self.title_label = Label(self, text=text, height=3, width=100, bg='grey')
        self.title_label['font'] = 'Helvetica -32'
        self.title_label.pack()

    def refresh_mutilistbox(self):
        pass

    def add_status(self):
        self.status_frame = Status(self)
        self.status_frame['relief'] = 'groove'
        self.status_frame['borderwidth'] = 2
        self.status_frame.pack(fill=Tkinter.BOTH)
        self.status_frame.message_button['command'] = lambda:self.panel_manager.switch_panel(self, 'message')
        self.status_frame.people_button['command'] = lambda:self.panel_manager.switch_panel(self, 'people')
        self.status_frame.apply_button['command'] = lambda:self.panel_manager.switch_panel(self, 'applys')

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
        client_type = ['', '信贷员', '主管', '副行长', '行长']
        self.status_text_label = Label(self, text='当前用户>%s 当前>%s' % ('%s(%s)' % (const.user_name, client_type[int(const.user_type)] if const.user_type else None), const.panel_type), width=80)
        self.status_text_label['anchor'] = 'e'
    
    def set_status_text(self, text_tuple):
        self.status_text_label['text'] = '当前用户>%s 当前>%s' % text_tuple

    def pack_all(self):
        self.message_button.pack(side=Tkinter.LEFT)
        self.apply_button.pack(side=Tkinter.LEFT)
        self.people_button.pack(side=Tkinter.LEFT)
        self.status_text_label.pack()

