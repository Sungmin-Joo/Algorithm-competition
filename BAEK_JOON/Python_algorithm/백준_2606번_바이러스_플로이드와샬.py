import sys
input=sys.stdin.readline
INF = 2147483647

def set_arr_info(n, m):
    arr = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        start, end = map(int, input().split())
        arr[start - 1][end - 1] = 1
        arr[end - 1][start - 1] = 1
    return arr

def floyd_algorithm(arr, n, m):
    for middle_city in range(n):
        for start in range(n):
            if start == middle_city:
                arr[start][middle_city] = 0
                continue
            for end in range(n):
                arr[start][end] = min(arr[start][middle_city] + arr[middle_city][end], arr[start][end])
                #사실 이 부분은 그렇게 중요하진 않지만 플로이드 와샬 알고리즘에는 손 대기 싫어서 유지해둠.
    return arr

if __name__ == "__main__":
    # 도시 갯수 입력
    n = int(input())
    # 간선 갯수 입력
    m = int(input())

    # 도시와 간선에 대한 정보를 입력.
    arr = set_arr_info(n, m)
    arr = floyd_algorithm(arr, n, m)
    #1번 노드에서 갈 수 있는곳을 찾아서 카운트
    cnt = 0
    for i in arr[0]:
        if i != INF:
            cnt += 1
    print(cnt - 1)#0도 세짐