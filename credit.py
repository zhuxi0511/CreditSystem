#coding: utf-8

import sys
import Tkinter
from model.panel import PanelManager
from model.login import Login
from model.message import Message
from model.apply import Apply
from model.people import People, PeopleInformationToplevel
from model.model import init
from model import const

def credit():
    root = Tkinter.Tk()
    root.geometry('800x600')
    root.title('对公信贷系统')
    root.option_add("*Font", "helvetica -12")
    login = Login(master=root)
    login.pack()
    #p = PeopleInformationToplevel()

    people = People(master=root)
    message = Message(master=root)
    applys = Apply(master=root)
    panel_manager = PanelManager(login, people, message, applys)

    root.mainloop()


def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    init()
    credit()

if __name__ == '__main__':
    main()
