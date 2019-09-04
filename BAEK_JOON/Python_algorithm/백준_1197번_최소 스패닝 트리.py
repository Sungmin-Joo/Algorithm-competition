import sys
input = sys.stdin.readline

#부모 노드를 찾는 함수
def getParent(arr, n):
    if arr[n] == n: return n
    return getParent(arr,arr[n])


#두 부모 노드를 합치는 함수
def unionParent(arr,n_1, n_2):
    n_1 = getParent(arr,n_1)
    n_2 = getParent(arr,n_2)
    if n_1 < n_2 : arr[n_2] = n_1
    else: arr[n_1] = n_2

#같은 부모를 가지는지 확인
def findParent(arr, n_1, n_2):
    n_1 = getParent(arr,n_1)
    n_2 = getParent(arr,n_2)
    if n_1==n_2: return 1
    else : return 0

edges = []
parent = {}
V, E = map(int,input().split())
for _ in range(E):
    edges.append([*map(int,input().split())])

for i in range(V):
    parent[i+1] = i+1

edges.sort(key=lambda val: val[2])

MST = []
#Kruskal's  Algorithm
for e in edges:
    v, u, w = e
    if findParent(parent, v, u) == 0:
        unionParent(parent,v,u)
        MST.append(e)

print(sum([w for v, u, w in MST]))