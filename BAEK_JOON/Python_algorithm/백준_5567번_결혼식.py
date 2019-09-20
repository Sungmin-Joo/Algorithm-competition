import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = {}
for key in range(n):
    arr[key+1] = []
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

visit = [0] * (n+1)
cnt = 0
for i in arr[1]:
    if visit[i] == 0:
        visit[i] = 1
        cnt += 1
    for j in arr[i]:
        if j == 1:
            continue
        if visit[j]:
            continue
        visit[j] = 1
        cnt += 1
print(cnt)
