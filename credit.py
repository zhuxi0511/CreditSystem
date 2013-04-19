#coding: utf-8

import Tkinter
from model.util import Show_style
from model.login import Login
from model.message import Message
from model.apply import Apply
from model.people import People

def credit():
    root = Tkinter.Tk()
    root.geometry('800x600')
    root.title('对公信贷系统')
    root.option_add("*Font", "helvetica -12")
    people = People(master=root)
    people.pack()
    """
    message = Message(master=root)
    message.pack()
    applys = Apply(master=root)
    applys.pack()
    login = Login(master=root)
    login.pack()
    """

    root.mainloop()


if __name__ == '__main__':
    credit()
