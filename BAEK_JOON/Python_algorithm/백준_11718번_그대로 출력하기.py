# -*- coding: utf-8 -*-
while(1):
    try:
        text = input()
    except EOFError:
        break
    else:
        print (text)