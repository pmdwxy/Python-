# !/usr/bin/env python3
# -*- coding: utf-8 -*-

print('这是一个猜年龄的游戏~')
print('您有三次机会猜测，每次输入所猜年龄后回车~')
print('系统会告知您猜大了还是小了，猜对即结束游戏！')
age = 19
count = 0
while True:
    count = count + 1
    GuessAge = input('您猜测的年龄大小为：')
    if age>int(GuessAge)and count<3:
        print('猜小了，换个大点的~~')
        continue
    elif age<int(GuessAge) and count<3:
        print('猜大了，换个小点的~~')
        continue
    elif age==int(GuessAge):
        print('恭喜！猜对了！')
        break
    elif count==3:
        print('遗憾3次都没对~')
        ans = input('继续(Y/y)，还是不继续(N/n)？:')
        if ans == 'Y' or ans == 'y':
            count = 0
            continue
        elif ans == 'N' or ans == 'n':
            break
    else:
        continue

