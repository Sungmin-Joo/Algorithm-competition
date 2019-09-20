import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, w = map(int,input().split())
    arr[parent].append((child, w))
    arr[child].append((parent, w))

def DFS(v):
    node = 0
    m = 0
    q = deque()
    visited = [False] * (n+1)
    visited[v[0]] = True
    q.append(v)
    while q:
        v = q.popleft()
        for edge in arr[v[0]]:
            if visited[edge[0]] == False:
                visited[edge[0]] = True
                q.append((edge[0],v[1]+edge[1]))
                if v[1] + edge[1] > m:
                    m = v[1] + edge[1]
                    node = edge[0]
    return node, m


print( DFS((DFS((1,0))[0], 0))[1])
#참고 : https://home-body.tistory.com/425