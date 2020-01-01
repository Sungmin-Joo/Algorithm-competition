import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [[ 0 for i in range(n + 1)] for j in range(n + 1)]

for _ in range(k):
    r, c = map(int, input().split())
    arr[r][c] = 1
    arr[r][0] += 1
    arr[0][c] += 1

def find_r_c():
    idx = [0, 0]
    num = 0
    for i in range(1, n + 1):
        if num < arr[0][i]:
            num = arr[0][i]
            idx = [0, i]
        if num < arr[i][0]:
            num = arr[i][0]
            idx = [i, 0]
    return idx

def find_max():
    cnt = [0, 0]
    for i in range(1, n + 1):
        if arr[0][i] == 0:
            cnt[1] += 1
        if arr[i][0] == 0:
            cnt[0] += 1
    return n - max(cnt)

def remove_element(m):
    if m[0] == 0:
        for i in range(1, n + 1):
            arr[i][m[1]] = 0
            arr[i][0] -= 1
    elif m[1] == 0:
        for i in range(1, n + 1):
            arr[m[0]][i] = 0
            arr[0][i] -= 1
    arr[m[0]][m[1]] = 0

ans = 0
maximum = find_max()
while 1:
    m = find_r_c()
    if m == [0, 0]: break
    ans += 1

    remove_element(m)

print(ans if ans < maximum else maximum)