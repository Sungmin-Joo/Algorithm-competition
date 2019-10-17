import sys
input=sys.stdin.readline


if __name__ == "__main__":
    for test in range(int(input())):
        n = int(input())
        arr = [[0]*n,[0]*n]
        dp = [[0]*n,[0]*n]
        for idx, var in enumerate(map(int,input().split())):
            arr[0][idx] = var
        for idx, var in enumerate(map(int,input().split())):
            arr[1][idx] = var

        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]

        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1] + arr[0][i], dp[1][i-2] + arr[0][i])
            dp[1][i] = max(dp[0][i-1] + arr[1][i], dp[0][i-2] + arr[1][i])
        print(max(dp[0][n-1], dp[1][n-1]))