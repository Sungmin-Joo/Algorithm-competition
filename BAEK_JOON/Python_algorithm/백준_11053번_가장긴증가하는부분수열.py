import sys
input = sys.stdin.readline
global dp, l

n = int(input())
arr = [*map(int,input().split())]
dp = [0] * n
m = 0
for i in range(n):
    if i == 0:
        dp[i] = 1
    else:
        max_dp = 0
        for j in range(0, i):
            if max_dp < dp[j] and arr[j] < arr[i]:
                max_dp = dp[j]
        dp[i] = max_dp+1
print(max(dp))