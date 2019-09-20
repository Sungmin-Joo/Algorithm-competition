import sys
input = sys.stdin.readline
n, m = map(int,input().split())

arr = [*map(int,input().split())]
arr.sort(reverse=True)
h_max = arr[0]
h_min = 0
result = 0
while h_min < h_max :
    s = 0
    mid = (h_max + h_min)//2
    for i in range(n):
        if arr[i] - mid <= 0:
            break
        s += arr[i] - mid
    if s < m:
        h_max = mid
    else:
        h_min = mid + 1
        result = mid

print(result)