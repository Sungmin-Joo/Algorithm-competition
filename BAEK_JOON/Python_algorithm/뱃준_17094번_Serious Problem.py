# -*- coding: utf-8 -*-
N = input()
s = input()
c_2=s.count('2')
c_e=s.count('e')
if(c_e == c_2):
    print('yee')
else:
    print(['e','2'][(c_2 > c_e)])