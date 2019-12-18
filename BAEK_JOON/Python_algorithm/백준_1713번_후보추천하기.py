n = int(input())
num = int(input())

def is_in_arr(arr , w):
    for i in arr:
        if i[2] == w:
            return True
    return False

arr = []
who = input().split()
for idx, w in enumerate(who):
    if is_in_arr(arr, w):
        for index, var in enumerate(arr):
            if var[2] == w:
                arr[index][0] += 1
                break
    else:
        if len(arr) < n:
            arr.append([1, idx, w])
        else:
            arr[0] = [1, idx, w]

    arr.sort(key=lambda x: (x[0], x[1]))

arr.sort(key=lambda x:int(x[2]))
for i in range(n):
    if i == n-1:
        print(arr[i][2])
    else:
        print(arr[i][2], end = ' ')