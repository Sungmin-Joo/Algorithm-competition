import sys
input = sys.stdin.readline

s = int(input())
n = 1
t_s = 0
while 1:
    if t_s > s:
        break
    t_s += n
    n += 1
print(n-2)