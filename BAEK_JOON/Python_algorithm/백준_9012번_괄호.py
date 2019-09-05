# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:20:59 2019

@author: 주성민
"""
#import sys
#input = sys.stdin.readline
n = int(input())

for _ in range(n):
    flag = 1
    arr=[]
    for i in input():
        if i == '(':
            arr.append(i)
        else:
            if arr == []:
                flag = 0
            else:
                arr.pop()
    if flag and arr != []:
        flag = 0
    print("YES" if flag else "NO")
            