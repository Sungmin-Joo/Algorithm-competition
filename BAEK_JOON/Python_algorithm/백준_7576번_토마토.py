import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())

arr = []
deq = deque()
visit = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    arr.append([*map(int, input().split())])

for i in range(n):    
    for j in range(m):
        if arr[i][j] == 1:
            deq.append((i, j))
            visit[i][j] = 1
        
flag = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag = 0
            break

if flag and deq:
    print(0)
    exit(0)


d_x = [0, 0, 1, -1]
d_y = [1, -1, 0, 0]
ans = 0

while 1:
    deq_second = deque()
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if not(0 <= new_x < n and 0 <= new_y < m): continue
            if visit[new_x][new_y] or arr[new_x][new_y] != 0: continue
            deq_second.append((new_x, new_y))
            visit[new_x][new_y] = 1
            arr[new_x][new_y] = 1
    deq = deq_second
    if not deq: break
    ans += 1

for i in range(n):
    if 0 in arr[i]:
        print(-1)
        exit(0)
print(ans)