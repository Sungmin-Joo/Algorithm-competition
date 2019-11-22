from itertools import combinations
from math import gcd

def lcm(a, b):
    return a*b // gcd(a, b)
n, k = map(int, input().split())
arr = [*map(int, input().split())]
visit = {1:0}
answer = n

if k > 1:
    for i in combinations(arr,2):
        a, b = i
        num = lcm(a,b)
        for j in range(num, n, num):
            visit[j+1] = 0

for i in arr:
    for j in range(1, n+1, i):
        if j in visit.keys():
            if visit[j] == 0:
                visit[j] = 1
                answer -= 1
        else:
            answer -= 1
print(answer)
