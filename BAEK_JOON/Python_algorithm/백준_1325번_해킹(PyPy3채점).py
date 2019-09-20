import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [[] for _ in range(n+1)]
visit = []
cnt = 0

for _ in range(m):
    e, s = map(int,input().split())
    arr[s].append(e)

def BFS(k):
    global cnt
    q = deque()
    q.append(k)
    cnt = 0
    visit[k] = True
    while q:
        x = q.popleft()
        for k in arr[x]:
            if visit[k] is False:
                q.append(k)
                visit[k] = True
                cnt += 1

'''
def DFS(k,cnt):
    check[k] = True
    for i in arr[k]:
        if check[i] == False:
            cnt = DFS(i, cnt)
            check[i] = True
    return cnt + 1
'''
m = 0
answer = []
for k in range(1, n+1):
    visit = [False for _ in range(n+1)]
    #cnt = DFS(k, 0)
    BFS(k)
    if cnt > m :
        m = cnt
        answer.clear()
        answer.append(k)
    elif cnt == m:
        answer.append(k)
print(" ".join(map(str, answer)))