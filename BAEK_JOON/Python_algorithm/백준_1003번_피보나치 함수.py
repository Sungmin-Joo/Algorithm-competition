# -*- coding: utf-8 -*-
import sys
IN=sys.stdin.readline
d=[0]*41
d[0],d[1]=(1,0),(0,1)
def fi(n):
    if(d[n]!=0):
        return d[n]
    else:
        a,b=fi(n-1),fi(n-2)
        d[n]=(a[0]+b[0],a[1]+b[1])
        return d[n]

for _ in range(int(IN())):
    n=int(IN())
    print(' '.join(map(str,fi(n))))
"""
Created on Wed Aug  7 16:32:25 2019

@author: 주성민
"""