# !/usr/bin/env python3
# -*- coding: utf-8 -*-
total = 0
with open('a.txt','r+') as f:
    f.seek(0)
    while True:
        data = f.readline().split(' ')
        #print (data,len(data))
        if len(data)==1:
            break
        else:
            num = int(data[1])
            price = int(data[-1])
            total = total+num*price


print('此次购物总花费：%s 元' %total)

