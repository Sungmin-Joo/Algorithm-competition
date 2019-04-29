# -*- coding: utf-8 -*-
for i in range(int(input())):
    A = input()
    l = len(A)//2
    if(A[l-1] != A[l]):
        print("Do-it-Not")
    else:
        print("Do-it")