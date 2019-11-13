import sys
input=sys.stdin.readline
n = int(input())
while 1:
    num = int(input())
    if num == 0: break
    if num % n != 0: print("%d is NOT a multiple of %d." %(num, n))
    else : print("%d is a multiple of %d." %(num, n))
