import sys
input=sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    arr = [[] for _ in range(n+1)]
    visit = [False for _ in range(n+1)]

    for _ in range(m):
        start, end = map(int, input().split())
        arr[start].append(end)
        arr[end].append(start)

    cnt = 0
    q = [arr[1]]
    while q:
        for node in q.pop(0):
            if not visit[node] :
                visit[node] = True
                if node != 1:
                    cnt += 1
                q.append(arr[node])
    print(cnt)
