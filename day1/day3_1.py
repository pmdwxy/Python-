# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
name = " alberT"
name1=name.strip()
print(name.strip())
print(name1[0:2]=='al')
print(name1[-1]=='T')
print(name1.replace('l','p'))
print(name1.split('l'))
print(name1.upper())
print(name1.lower())
print(name1[1])
print(name1[0:3])
print(name1[-1:-3:-1])
print(name1.find('e'))
print(name1[:-1])
#列表练习
data=['albert',18,[2000,1,1]]
name_list = data[0]
age_list = data[1]
birthDate = data[2][-1]
birthMonth = data[2][-2]
birthYear = data[2][-3]
print(name_list,age_list,birthDate,birthMonth,birthYear)
l1 = {
    'name': 'albert',
    'age': 18,
    'gender': 'male'
}

res = l1.pop('name') #删除指定key的value，并拿到一个返回值
print(res)
print(l1)