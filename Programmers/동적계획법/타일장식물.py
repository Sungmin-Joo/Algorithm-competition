def solution(N):
    dp = [[4,1], [6,1]]
    if N < 3:
        return dp[N-1][0]
    for i in range(2,N):
        w = dp[i-1][1] + dp[i-2][1]
        dp.append([dp[i-1][0] + (w << 1),w])
      
    return dp[N-1][0]