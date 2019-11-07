import sys
input=sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m = 1
visit = [False for i in range(26)]
r, c = map(int,input().split())
arr = []
for _ in range(r):
    arr.append(list(input().rstrip()))
dp = [[0 for i in range(c)] for i in range(r)]


def dfs(x, y, step):
    global m
    visit[ord(arr[y][x])-65] = True
    step += 1
    for i in range(4):
        new_x = dx[i] + x
        new_y = dy[i] + y

        if not( (0 <= new_x < c) and (0 <= new_y < r)): continue
        new_alpha = arr[new_y][new_x]
        if visit[ord(new_alpha)-65]: continue

        m = max(m, step + 1)
        dfs(new_x, new_y, step)
    step -= 1
    visit[ord(arr[y][x])-65] = False
dfs(0,0,0)
print(m)