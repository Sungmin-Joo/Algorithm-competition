import queue
import sys
input = sys.stdin.readline
w = [[1,0],[0,1],[-1,0],[0,-1]]
arr = []
n = int(input())

arr = [[0]*n for i in range(n)]
visited = [[True]*n for i in range(n)]
for i in range(n):
    temp = input().split()[0]
    for j in range(n):
        arr[i][j] = int(temp[j])
q=queue.Queue()

def BFS():
    cnt = 0
    len_arr = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] :
                visited[i][j] = False
                if arr[i][j] :
                    q.put([i,j])
                    cnt += 1
                    while not q.empty():
                        x, y = q.get()
                        for w_i, w_j in w:
                            t_i = x+w_i
                            t_j = y+w_j
                            if t_i < 0 or t_j < 0 or t_i > n-1 or t_j > n-1:
                                continue
                            if visited[t_i][t_j]:
                                if arr[t_i][t_j] :
                                    q.put([t_i,t_j])
                                    cnt += 1
                                visited[t_i][t_j] = False
                    len_arr.append(cnt)
                    cnt = 0
    return len_arr
answer = BFS()
answer.sort()
print(len(answer))
for i in answer:
    print(i)