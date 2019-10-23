from math import factorial as fc
a,b=map(int,input().split())
print((fc(a)//(fc(b)*fc(a-b))))