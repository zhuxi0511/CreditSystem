#coding: utf-8

import const
from panel import PanelManager
from message import Message
from apply import Apply
from people import People

def init():
    f = open('data/login')
    if f:
        const.login_dict = get_login_dict(f.readlines())
    else:
        print 'login file error'
        raise Exception()


def login_model(user, password):
    user = user.strip()
    print const.login_dict
    pa = const.login_dict.get(user)
    if pa:
        return pa[1] == password, pa[0]
    else:
        return None, None

def get_login_dict(lines):
    ret = {}
    for line in lines:
        line = line.strip().split()
        ret[line[1]] = (line[0], line[2])
    return ret
