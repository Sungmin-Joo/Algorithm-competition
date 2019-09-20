import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append([e, s])
arr.sort()


end = 0
cnt = 0
for e_t, s_t in arr:
    if end <= s_t:
        cnt += 1
        end = e_t
print(cnt)