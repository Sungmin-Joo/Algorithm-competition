import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    cnt = 0
    q = deque()
    [q.append(i) for i in range(1,n+1)]
    while arr:
        if q[0] == arr[0]:
            arr.pop(0)
            q.popleft()
        else:
            if q.index(arr[0]) <= len(q)//2:
                while q[0] != arr[0] :
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != arr[0] :
                    q.appendleft(q.pop())
                    cnt += 1
    print(cnt)