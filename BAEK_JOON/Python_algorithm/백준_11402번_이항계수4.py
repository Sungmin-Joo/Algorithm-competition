import sys
input=sys.stdin.readline

if __name__ == "__main__":
    arr = [[0 for _ in range(2000)] for _ in range(2000)]
    n, k, m = map(int, input().split())

    for i in range(m):
        arr[i][0] = 1
        for j in range(1, i + 1):
            arr[i][j] = (arr[i-1][j-1] + arr[i-1][j])%m

    s = 1
    while n or k:
        s *= arr[n%m][k%m]
        n //= m
        k //= m
        s %= m

    print(s)