import sys
IN=sys.stdin.readline
n=int(IN())
arr=[*map(int,IN().split())]
dp=[0]*(n+1)

for i in range(1,n+1,1):
    dp[i]=max(arr[i-1],max(dp[j] + dp[i-j] for j in range(i-1,i//2-1,-1)))
print(dp[n])