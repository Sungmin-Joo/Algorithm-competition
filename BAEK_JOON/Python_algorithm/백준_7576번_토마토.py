import sys
input = sys.stdin.readline
#현재코드는 시간초과가 나는 코드
#전체적인 알고리즘 수정이 필요하다.
m, n = map(int, input().split())
arr = []
cnt_1 = 0
cnt_0 = 0
cnt_m1 = 0
total = m * n
for i in range(n):
    arr.append([])
    for j in [*map(int, input().split())]:
        if j == 1: cnt_1 += 1
        elif j == 0 : cnt_0 += 1
        else : cnt_m1 += 1
        arr[i].append(j)
if cnt_0 == 0:
    print(0)
    exit(0)


d_x = [0, 0, 1, -1]
d_y = [1, -1, 0, 0]
def solution():
    visit = [[0 for i in range(m)] for j in range(n)]
    return_num = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and arr[i][j] == 1:
                visit[i][j] = 1
                return_num += 1
                for z in range(4):
                    new_x = i + d_x[z]
                    new_y = j + d_y[z]
                    if 0 <= new_x < n and 0 <= new_y < m:
                        if visit[new_x][new_y] == 0 and arr[new_x][new_y] == 0:
                            arr[new_x][new_y] = 1
                            visit[new_x][new_y] = 1
                            return_num += 1
    return return_num

ans = 0
while 1:
    #전염 알고리즘 수행
    #더 이상 전염되는게 없다면 빠져나옴
    tmp = cnt_1
    cnt_1 = solution()
    if cnt_1 == tmp or cnt_1 == total - cnt_m1: break
    ans += 1
#최종 전염 횟수 -1을 출력
if cnt_1 != total - cnt_m1 : print(-1)
else : print(ans + 1)    
