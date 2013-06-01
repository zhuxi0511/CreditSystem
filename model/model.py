#coding: utf-8

import const
from copy import deepcopy

def init():
    f = open('data/login')
    if f:
        const.login_dict = get_login_dict(f.readlines())
    else:
        print 'login login file error'
        raise Exception()
    f = open('data/people')
    if f:
        const.people_information_list = get_people_list(f.readlines())
    else:
        print 'login people file error'
        raise Exception()
    f = open('data/apply')
    if f:
        const.apply_information_list = get_apply_list(f.readlines())
    else:
        print 'login people file error'
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

def get_people_list(lines):
    people_information_list = []
    for line in lines:
        line = line.strip().split('\t')
        for i, l in enumerate(line):
            if l == '#':
                line[i] = ''
        people_information_list.append(line)
    return people_information_list

def get_apply_list(lines):
    apply_information_list = []
    for line in lines:
        line = line.strip().split('\t')
        for i, l in enumerate(line):
            if l == '#':
                line[i] = ''
        apply_information_list.append(line)
    return apply_information_list

def save_people_information(people_information):
    const.people_information_list.append(people_information)
    f = open('data/people', 'w')
    print 'people list:', const.people_information_list
    print type(const.people_information_list)
    print people_information
    tmp = deepcopy(const.people_information_list)
    for j, line in enumerate(tmp):
        for i, l in enumerate(line):
            if l == '':
                tmp[j][i] = '#'
    f.writelines(map(lambda x:'\t'.join(x) + '\n', tmp))
    return True

def save_apply_information(apply_information):
    const.apply_information_list.append(apply_information)
    f = open('data/apply', 'w')
    print 'apply list:', const.apply_information_list
    tmp = deepcopy(const.people_information_list)
    for j, line in enumerate(tmp):
        for i, l in enumerate(line):
            if l == '':
                tmp[j][i] = '#'
    f.writelines(map(lambda x:'\t'.join(x) + '\n', tmp))
    return True

def show_people_list():
    people_list = []
    for line in const.people_information_list:
        print line
        people_list.append((line[0], line[1], line[2], line[5], line[10]))
    return people_list
