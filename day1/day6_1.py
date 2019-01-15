# !/usr/bin/env python3
# -*- coding: utf-8 -*-

math = {
    '第1章 集合和命题':{
        '集合':{
            '1.1':'集合及其表示法',
            '1.2':'集合之间关系',
            '1.3':'集合的运算',
        },
        '四种命题形式':{
            '1.4':'命题的形式及等价关系',
        },
        '充分条件与必要条件':{
            '1.5':'充分条件，必要条件',
            '1.6':'子集与推出关系'
        }
    },
    '第2章 不等式':{
        '基本不等式':{
            '2.1':'不等式基本性质',
            '2.2':'一元二次不等式',
        },
        '其他不等式':{
            '2.3':'其他不等式解法',
            '2.4':'不等式及其应用',
            '2.5':'不等式证明'
        }
    },
    '第3章 函数基本性质':{
        '函数概念与建立':{
            '3.1':'函数的概念',
            '3.2':'函数关系建立',
        },
        '函数运算与性质':{
            '3.3':'函数的运算',
            '3.4':'函数的基本性质',
        }
    },
    '第4章 幂函数，指数函数和对数函数':{
        '幂函数':{
            '4.1':'幂函数的性质与图像',
        },
        '指数函数':{
            '4.2':'指数函数图像与性质',
            '4.3':'借助计算器观察函数递增的快慢',
        },
        '对数':{
            '4.4':'对数概念及其运算',

        },
        '反函数':{
            '4.5':'反函数的概念',
        },
        '对数函数':{
            '4.6':'对数函数图像与性质',
        },
        '指数方程和对数方程':{
            '4.7':'简单的指数方程',
            '4.8':'简单的对数方程',
        }
    }

}

#print(math)

Chapter_list = list(math.keys())             #章列表

while True:
    print(" 章 ".center(50,'*'))
    for i in Chapter_list:
        print(Chapter_list.index(i)+1,i)       #打印章列表
    cha_id = input("请输入章编号,或输入q(quit)退出：")   #章ID
    if cha_id.isdigit():
        cha_id = int(cha_id)
        if 0 < cha_id <= len(Chapter_list):
            cha_name = Chapter_list[cha_id-1]     #根据章ID获取章名称
            Section_list = list(math[cha_name].keys())    #根据章名称获取对应的值，从新字典中获取key，即节列表
            while True:
                print(" 节 ".center(50,'*'))
                for v in Section_list:
                    print(Section_list.index(v)+1,v)       #打印节列表
                section_id = input("请输入节编号,或输入b(back)返回上级菜单，或输入q(quit)退出：")
                if section_id.isdigit():
                    section_id = int(section_id)
                    if 0 < section_id <= len(Section_list):
                        section_name = Section_list[section_id-1]    #根据节ID获取节名称
                        Subsection_list =  list(math[cha_name][section_name].keys())   #根据章名称获取对应的值，从新字典中获取值，即子节列表
                        while True:
                            print(" 子节 ".center(50,'*'))
                            for j in Subsection_list:
                                print(Subsection_list.index(j)+1,j)
                            Subsection_id = input("请输入子节编号，或输入b(back)返回上级菜单，或输入q(quit)退出：")
                            if Subsection_id.isdigit():
                                Subsection_id = int(Subsection_id)
                                if 0 < Subsection_id <= len(Subsection_list):
                                    Subsection_name = Subsection_list[Subsection_id - 1]  # 根据节ID获取节名称
                                    print(math[cha_name][section_name][Subsection_name])
                            elif Subsection_id == 'b':
                                break                #终止此层while循环，跳转到上一层While。
                            elif Subsection_id == 'q':
                               # flag1 = True
                               # break               #根据标志位结束程序。
                                exit()
                            else:
                                print("输入非法！")
                    else:
                        print("编号%d不存在。"%section_id)
                elif section_id == 'b':
                    break
                elif section_id == 'q':

                    exit()
                else:
                    print("输入非法!")

        else:
            print("编号%d不存在。"%cha_id)
    elif cha_id == 'q':
        break
    else:
        print("输入非法!")