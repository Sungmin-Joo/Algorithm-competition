import sys
input = sys.stdin.readline
n1, n2, n3 = map(int, input().split())
arr = {}
cnt = 0

for _ in range(n1):
    tmp = input().rstrip()
    arr[tmp] = 1

for _ in range(n2):
    tmp = input().rstrip()
    if arr.get(tmp, None) == None:
        arr[tmp] = 1
    else:
        arr[tmp] += 1
for _ in range(n3):
    tmp = input().rstrip()
    try:
        arr[tmp] += 1
    except:
        continue

answer = []

for k, v in arr.items():
    if v >= 2:
        cnt += 1
        answer.append(int(k))

print(cnt)
answer.sort()
for i in answer:
    print(i)
