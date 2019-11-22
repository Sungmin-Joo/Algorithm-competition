import heapq
import sys
input = sys.stdin.readline


arr = []
for i in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort()

que = []
heapq.heappush(que, 0)
for s, e in arr:
    if que[0] > s: heapq.heappush(que, e)
    else:
        heapq.heappop(que)
        heapq.heappush(que, e)

print(len(que))