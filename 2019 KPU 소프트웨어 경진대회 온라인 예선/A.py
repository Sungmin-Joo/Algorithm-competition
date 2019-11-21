arr = [*map(int, input().split())]
arr.sort()
arr = list(set(arr))
l = len(arr)
answer = "NO"
if l < 3:
    print(answer)
    exit(0)

for i in range(l):
    if i >= l or i + 3 >= l: break
    if arr[i] > arr[i+3]:
        if arr[i] - arr[i+3] == 3:
            answer = "YES"
            break
    else:
        if arr[i+3] - arr[i] == 3:
            answer = "YES"
            break
print(answer)