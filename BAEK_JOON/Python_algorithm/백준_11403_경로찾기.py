import sys
input=sys.stdin.readline

def BFS(i, arr, n):
    visit=[0] * n
    q=[i]

    while q:
        index=q.pop(0)
        for i, v in enumerate(arr[index]):
            if visit[i] == 0 and v == 1:
                visit[i] = 1
                q.append(i)

    return visit

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append([*map(int,input().split())])
    for i in range(n):
        print(' '.join(map(str,BFS(i,arr,n))))
