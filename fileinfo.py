"""
Created on Wed Apr 24 21:14:04 2019

@author: Zhang-haoze
"""

a = int(input())   #输入大佬的步长
b = int(input())    #输入助教x的步长
m=a*b             #先将二者相乘，以便进行后续计算
def s(a,b):         #建立一个递归函数
    if a%b!=0:     #利用欧几里得算法算最大公约数
        c=a%b
        return s(b,c)
    else:
        return b
    
    
