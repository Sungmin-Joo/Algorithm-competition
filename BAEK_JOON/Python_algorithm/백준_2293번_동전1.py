import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0 for i in range(10001)]
c = [0 for i in range(101)]

dp[0] = 1
for i in range(1, n + 1):
    c[i] = int(input())
    for j in range(c[i], k + 1, 1):
        #원래 j원을 만드는 경우 + 입력받은 코인을 이용해서 j원을 만드는 경우
        dp[j] = dp[j] + dp[j - c[i]]
        #위 수식을 k원을 만드는 경우까지 수행
print(dp[k])
