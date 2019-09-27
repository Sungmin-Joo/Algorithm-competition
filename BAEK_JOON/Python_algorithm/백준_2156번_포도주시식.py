import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = [0 for i in range(N+1)]
    dp = [0 for i in range(N+1)]

    for i in range(1,N+1):
        num = int(input())
        arr[i] = num
        if i < 3:
            if i == 1:
                dp[1] = num
            else:
                dp[2] = num + dp[1]
        else:
            dp[i] = max(dp[i-2] + arr[i], arr[i-1]+dp[i-3] + num,dp[i-1])

    print(dp[N])