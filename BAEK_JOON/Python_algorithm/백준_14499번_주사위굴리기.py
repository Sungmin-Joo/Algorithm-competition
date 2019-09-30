import sys
input = sys.stdin.readline

d_a = [(0,1),(0,-1),(-1,0),(1,0)]
d = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}

def replace(n):
    if n == 1 :
        d[1], d[3], d[4], d[6] = d[4], d[1], d[6], d[3]
    elif n == 2:
        d[1], d[3], d[4], d[6] = d[3], d[6], d[1], d[4]
    elif n == 3:
        d[1], d[2], d[5], d[6] = d[5], d[1], d[6], d[2]
    else:
        d[1], d[2], d[5], d[6] = d[2], d[6], d[1], d[5]

n, m, x, y, k = map(int,input().split())
arr = []
for i in range(n):
    arr.append([*map(int,input().split())])
for c in [*map(int,input().split())]:
    t_x = d_a[c-1][0] + x
    t_y = d_a[c-1][1] + y
    if (0 <= t_x < n) and (0 <= t_y < m):
        x, y = t_x, t_y
        replace(c)
        if arr[x][y] != 0:
            d[6] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = d[6]
        print(d[1])