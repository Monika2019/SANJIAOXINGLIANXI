# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Steven Lu

# 目的:
#22玩转三角形
a  = float(input("输入三角形第一边长 a =: "))
b  = float(input("输入三角形第二边长 b =: "))
c  = float(input("输入三角形第三边长 c =: "))

if ( a + b > c )and ( a + c > b ) and ( c + b > a ):
    if (abs(a-b)>=c)or(abs(a-c)>=b)or(abs(b-c)>=a):
        print("错误!某两边之差大于等于第三边，所以无法组成三角形。 ")
    else:
        if(a==b)or(b==c)or(a==c):
            print("正确!可以组成等边或等腰三角形。")
        else:
            print("正确!可以组成不等边三角形。")
else:
    print("错误!某两边之和小于等于第三边，所以无法组成三角形。 ")
