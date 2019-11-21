import sys
import copy
input = sys.stdin.readline



n = int(input())
arr_src = []
arr_des = []
for i in range(n):
    arr_src.append(input().split())
for i in range(n):
    arr_des.append(input().split())

def find_col():
    head_src = copy.deepcopy(arr_src[0])
    head_des = copy.deepcopy(arr_des[0])
    full_cnt = 0
    while full_cnt != n:
        pnt = 0
        idx = 0
        for i in range(n):
            if head_des[i] == head_src[i]:
                pnt += 1
            else:
                idx = i
        if pnt == n-1: return idx
        head_des = head_des[-1:] + head_des[:-1]
        full_cnt += 1
    return -1
def spin_row(idx, arr):
    arr[idx] = arr[idx][-1:] + arr[idx][:-1]

def spin_col(idx, arr, flag = 1):
    if flag:
        m = 0
        key = arr[m][idx]
        while m < n - 1:
            arr[m][idx] = arr[m+1][idx]
            m += 1
        arr[m][idx] = key
    else:
        m = n-1
        key = arr[m][idx]
        while m > 0:
            arr[m][idx] = arr[m-1][idx]
            m -= 1
        arr[m][idx] = key


idx = find_col()
if idx == -1:
    print("NO")
    exit(0)
answer = [idx + 1]
tmp_arr = copy.deepcopy(arr_src)
spin_col(idx, tmp_arr)
flag = 0
for i in range(n):
    for j in range(n):
        if tmp_arr[i] == arr_des[i]:
            flag +=1
            break
        else:
            spin_row(i, tmp_arr)
            answer.append(i+1)

if flag == n:
    print("YES")
    l = len(answer)
    for i, v in enumerate(answer):
        if i == l - 1: print(v, end = '\n')
        else: print(v, end = ' ')
    exit(0)

spin_col(idx, arr_src,0)
answer = [(idx + 1) * -1]
flag = 0
for i in range(n):
    for j in range(n):
        if arr_src[i] == arr_des[i]:
            flag +=1
            break
        else:
            spin_row(i, arr_src)
            answer.append(i+1)
if flag == n:
    print("YES")
    l = len(answer)
    for i, v in enumerate(answer):
        if i == l - 1: print(v, end = '\n')
        else: print(v, end = ' ')
    exit(0)
print("NO")