#coding:utf-8

import Tkinter
import const
from Tkinter import Frame, Label

class ApplySheetFrame(Frame):
    def __init__(self, master=None, apply_information=None):
        Frame.__init__(self, master)
        self.apply_information = apply_information
