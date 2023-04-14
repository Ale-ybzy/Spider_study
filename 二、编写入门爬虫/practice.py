# ！/usr/bin/python
# coding :utf-8


# 试题1 循环打印输出0-100之间所有奇数
'''
number = 1
while number < 101:
    if (number % 2 != 0):
        print(number, end=' ')  # end=''输出不换行
    number += 1;
'''

# 试题2 请将字符串“你好$$$我正在学 Python@#@#现在需要&*&*&修改字符串”中的符号变成一个空格，需要输出的格式为：
# “你好 我正在学 Python 现在需要 修改字符串”
'''
import re  # 正则表达式包

s_char = r'你好$$$我正在学 Python@#@#现在需要&*&*&修改字符串'  #单引号r不转义
# 去除特殊字符，只保留汉字，字母、数字
# sub(pattern,repl,string) 把字符串中的所有匹配表达式pattern中的地方替换成repl
d_char = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])"," ", s_char)
print(d_char)
'''

# 试题3 输出9*9乘法口诀表
'''
for a in range(1,10):
    for b in range(1,10):
        print('%d*%d =' % (a,b),a*b,end=" ")
        if (a == b):
            print()
            break
'''

# 试题4 写函数发放奖金
