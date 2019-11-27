import sys; input = sys.stdin.readline; sys.setrecursionlimit(1000000)

N = int(input())
A = [0] + [int(x) for x in input().split()]
D = [[-1 for _ in range(N+1)] for _ in range(N+1)]

def go(i, j):
    if i == j:
        return 1
    if i + 1 == j:
        if A[i] == A[j]:
            return 1
        else:
            return 0
    if D[i][j] >= 0: return D[i][j]
    if A[i] != A[j]: D[i][j] = 0; return D[i][j]
    else: D[i][j] = go(i+1, j-1); return D[i][j]

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(go(S, E))
#출처 : 백준 아이디 kyleoh95