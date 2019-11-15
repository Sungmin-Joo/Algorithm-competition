import sys
input=sys.stdin.readline
n = 0
for i in range(5):
    temp = int(input())
    if temp >= 40: n += temp
    else: n += 40
print(n//5)