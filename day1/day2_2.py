# !/usr/bin/env python3
# -*- coding: utf-8 -*-

count = 0
while count<3:
    count = count+1
    name = input('请输入用户名：')
    PassWord = input('请输入密码：')
    if name == 'Lucy' and PassWord == '123':
        print('输入正确，登录成功！')
        break
    else:
        print('用户名或码错误，请重新输入！剩余输入次数%s次' %(3-count))
        continue

if count == 3:
    print('您的账号被冻结！')