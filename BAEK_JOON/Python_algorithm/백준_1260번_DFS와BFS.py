import sys
IN=sys.stdin.readline

n,m,v=map(int,IN().split())
arr=[[] for i in range(n+1)]
visit=[]
def BFS(v):
    visit=[]
    q=[v]

    while q:
         temp=q.pop(0)
         if temp not in visit:
             visit.append(temp)
             t_q =list(set(arr[temp]) - set(visit))
             t_q.sort()
             q+=t_q
    return visit

def DFS(v):
    visit.append(v)
    for i in arr[v]:
        if i not in visit:
            DFS(i)
    return


for _ in range(m):
    x,y=map(int,IN  ().split())
    if not y in arr[x]:
        arr[x].append(y)
    if not x in arr[y]:
        arr[y].append(x)

for a in arr:
    a.sort()
DFS(v)
print(' '.join(map(str,visit)))
print(' '.join(map(str,BFS(v))),end='')
