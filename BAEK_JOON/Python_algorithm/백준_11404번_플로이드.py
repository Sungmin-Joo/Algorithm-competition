import sys
input=sys.stdin.readline
INF = 2147483647

def set_arr_info(n, m):
    arr = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        arr[start - 1][end - 1] = min(arr[start - 1][end - 1], cost)
    return arr

def floyd_algorithm(arr, n, m):
    for middle_city in range(n):
        for start in range(n):
            if start == middle_city:
                arr[start][middle_city] = 0
                continue
            for end in range(n):
                arr[start][end] = min(arr[start][middle_city] + arr[middle_city][end], arr[start][end])
    return arr

if __name__ == "__main__":
    # 도시 갯수 입력
    n = int(input())
    # 버스 갯수 입력
    m = int(input())

    # 도시와 버스에 대한 정보를 입력.

    arr = set_arr_info(n, m)
    arr = floyd_algorithm(arr, n, m)

    for x in arr:
        for y in x:
            if y == INF:
                print(str(0) + ' ', end='')
            else:
                print(str(y) + ' ', end='')
        print()