import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 10
dp[0] = 1
dp[1] = 2
dp[2] = 4
for _ in range(t):
    n = int(input())
    if n > 2 and dp[n-1]:
        pass
    else:
        for i in range(3,n):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n-1])