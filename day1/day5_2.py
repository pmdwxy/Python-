# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

with open('a.txt') as read_f,open('a1.txt','w') as write_f:
    for line in read_f:
        line=line.replace('mac','linux')
        write_f.write(line)

os.remove('a.txt')
os.rename('a1.txt','a.txt')

with open('a.txt','r+') as f1:
    print(f1.read())