import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(input().split()[:-1])


def comp(a, b):
    for i in range(50):
        try:
            if arr[a][i] > arr[b][i]:
                arr[a], arr[b] = arr[b], arr[a]
                break
            elif arr[a][i] < arr[b][i]:
                break
        except:
            if len(arr[a]) > len(arr[b]):
                arr[a], arr[b] = arr[b], arr[a]
            break

length = (len(arr))
for i in range(length - 1):
    for j in range(length - i - 1):
        comp(j, j+1)
for i in arr:
    print(' '.join(i))
