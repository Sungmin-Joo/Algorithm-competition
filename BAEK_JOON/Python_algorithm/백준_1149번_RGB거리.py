import sys
IN=sys.stdin.readline
n=int(IN())
dp=[[0,0,0] for i in range(n)]
dp[0][0],dp[0][1],dp[0][2]=map(int,IN().split())

for i in range(1,n):
    r,g,b=map(int,IN().split())
    dp[i][0]=min(dp[i-1][1],dp[i-1][2]) + r
    dp[i][1]=min(dp[i-1][0],dp[i-1][2]) + g
    dp[i][2]=min(dp[i-1][0],dp[i-1][1]) + b
print(min(dp[n-1]))