import sys
input=sys.stdin.readline

def find_row(arr):
    cnt = 0
    row_cnt = 0
    for char in arr:
        if char == '.': cnt += 1
        else:
            if cnt >= 2:
                row_cnt += 1
                cnt = 0
            else: cnt = 0
    if cnt >= 2: return row_cnt + 1
    else: return row_cnt

def find_col(arr):
    col_cnt = 0
    l = len(arr)
    for i in range(l):
        cnt = 0
        for j in range(l):
            if arr[j][i] == '.' : cnt += 1
            else:
                if cnt >= 2:
                    col_cnt += 1
                    cnt = 0
                else: cnt = 0
        if cnt >= 2 : col_cnt += 1
    return col_cnt

if __name__ == "__main__":
    arr = []
    row_cnt, col_cnt = 0, 0
    for i in range(int(input())):
        arr.append([])
        for j in input().rstrip():
            arr[i].append(j)
        row_cnt += find_row(arr[i])

    col_cnt = find_col(arr)
    print(row_cnt, col_cnt)