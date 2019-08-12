import sys
IN=sys.stdin.readline
x,y,w,h=map(int,IN().split())
print(min(x,w-x,y,h-y))