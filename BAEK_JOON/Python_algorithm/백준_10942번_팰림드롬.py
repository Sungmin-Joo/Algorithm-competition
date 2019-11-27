import sys
input = sys.stdin.readline

def check_palindrome(arr, check_arr, n):
    for i in range(2, n):
        for j in range(1, n - i + 1):
            if (arr[j] == arr[j+i]) and check_arr[j+1][j+i-1]:
                check_arr[j][j+i] = check_arr[j+i][j] = True

n = int(input())
arr = [0] + [*map(int, input().split())]
m = int(input())

check_arr = [[False for i in range(n+1)] for j in range(n+1)]

for i in range(1, n+1):
    check_arr[i][i] = True
for i in range(1, n):
    if arr[i] == arr[i + 1]:
        check_arr[i][i + 1] = check_arr[i + 1][i] = True

check_palindrome(arr,check_arr, n)
for i in range(m):
    s, e = map(int, input().split())
    print(1 if check_arr[s][e] else 0)