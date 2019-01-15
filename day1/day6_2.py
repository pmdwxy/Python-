# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

"""
#需求:
    用户名和密码存放于文件中，格式为：Albert|Albert123
    启动程序后，先登录，登录成功则让用户输入工资,然后打印商品列表，失败则重新登录，
    超过三次则退出程序,并将用户名添加到黑名单，再次启动程序登陆该用户名，提示用户禁止登陆
    允许用户根据商品编号购买商品
    用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    可随时退出，退出时，打印已购买商品和余额
"""
#加载商品信息
Goods = []

with open('CellPhone.txt','r',encoding='gbk') as f0:
    f0.seek(0)
    while True:
        perPhone = f0.readline()
        #print(perPhone)
        if perPhone!='':
            item = ''.join(perPhone.split('   '))
            Goods.append(item.strip())
        else:
            break
#打开存储的真实用户登录信息
with open('UserPassword.txt','r') as f:
    data = f.read()
    data = data.split('|')
userName = data[0]
password = data[1]

print('请登录~')

count = 0

while True:
    nameLogin = input('请输入用户名：')
    pswLogin = input('请输入密码：')
    if os.path.exists('BlockList.txt'):
        with open('BlockList.txt', 'r') as f2:
           blockNames=f2.read()
    else:
        with open('BlockList.txt', 'w+') as f2:
           blockNames=f2.read()
    if nameLogin==userName and password==pswLogin and nameLogin not in blockNames:
        print('登录成功！')
        salary = input('请输入您的工资：')
        selectCount = 0  # 购买计数器
        Goods_select = []  # 购买商品信息
        itemNumber = []  # 购买商品数量
        unitPrice = []  # 购买商品单价
        total = 0  # 购买总金额
        while True:
            print(" 手机信息 ".center(50, '*'))
            for p in Goods:
                print(Goods.index(p) + 1, p)  # 打印节列表
            Goods_id = input("请输入商品编号，或输入c(continue)继续选择商品，或输入q(quit)退出：")

            if Goods_id.isdigit():
                Goods_id = int(Goods_id)
                if 0 < Goods_id <= len(Goods):

                    Goods_select.insert(selectCount,Goods[Goods_id - 1] ) # 根据ID获取商品信息
                    itemNumber.insert(selectCount,int(input('请输入购买该商品购买数量：')))
                    #print('您要购买%s，%s个！' %(Goods_select[selectCount],itemNumber[selectCount]))
                    priceRaw = Goods_select[selectCount].split('￥')
                    unitPrice.insert(selectCount,int(float(priceRaw[-1])))
                    total+=unitPrice[selectCount]*itemNumber[selectCount]
                    balance = int(salary)- total
                    print('此时您还有余额：%s 元。'%balance)
                    if balance>0:
                        confirm = input('是否购买？购买(Y/y)，放弃(N/n).')
                        if confirm == 'Y' or confirm == 'y':
                            print('您已购买%s，%s个！' % (Goods_select[selectCount], itemNumber[selectCount]))
                            print('还有余额%s元。'%balance)
                        else:
                            print('您已放弃购买！购买清单如下：')
                            info_purchase = [[i, j] for i, j in zip(Goods_select, itemNumber)]
                            print("购买信息".center(30,'*'),"数量".center(6,'*'))
                            for item_info in info_purchase:
                                print(item_info[0].center(30,' '),str(item_info[1]).center(5,' '))


                            #print(info_purchase)
                            print('以上'.center(80,'-'))
                            print('总额：%s元, 余额：%s元'%(total,balance))
                            exit()
                    else:
                        print('余额不足，请重新选择。')
                        continue
                selectCount += 1
            elif Goods_id == 'c':
                continue  # 继续选择商品。
            elif Goods_id == 'q':
                print('结束程序！')
                info_purchase = [[i, j] for i, j in zip(Goods_select, itemNumber)]
                print("购买信息".center(30, '*'), "数量".center(6, '*'))
                for item_info in info_purchase:
                    print(item_info[0].center(30, ' '), str(item_info[1]).center(5, ' '))

                # print(info_purchase)
                print('以上'.center(80, '-'))
                print('总额：%s元, 余额：%s元' % (total, balance))
                exit()
            else:
                print("输入非法！")
    elif nameLogin in blockNames:
        print('该用户在黑名单内，禁止登陆！')
        exit()
    elif count<=2:
        print('输入的用户名或密码错误，请重新输入！')
        count = count+1
        continue
    elif count>2:
        with open('BlockList.txt', 'a+') as f2:
            f2.write(nameLogin+'\n')
            print('输入错误三次，该用户已被拉入黑名单！')
            exit()