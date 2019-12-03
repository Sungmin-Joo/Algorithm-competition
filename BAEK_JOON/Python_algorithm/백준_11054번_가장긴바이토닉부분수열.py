n = int(input())
arr = [*map(int, input().split())]
dp = [0] * n
dp_re = [0] * n
cnt = 0

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] : dp[i] = max(dp[i], dp[j] + 1)

for i in range(n - 1, -1, -1):
    dp_re[i] = 1
    for j in range(n - 1, i -1, -1):
        if arr[j] < arr[i] : dp_re[i] = max(dp_re[i], dp_re[j] + 1)

for i in range(n):
    if cnt < dp[i] + dp_re[i] - 1: cnt = dp[i] + dp_re[i] - 1

print(cnt)
