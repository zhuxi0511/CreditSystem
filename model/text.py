#coding:utf-8

from Tkinter import * 
r = Tk()
root = Frame(r)
print root.pack_slaves()
Label(root,
    text = 'pack1',
    bg = 'red').pack(fill = Y) 
Label(root,
    text = 'pack2',
    bg = 'blue').pack(fill = Y) 
Label(root,
    text = 'pack3',
    height = 100,
    bg = 'green').pack(fill = X) 
print root.pack_slaves()
root.mainloop()
