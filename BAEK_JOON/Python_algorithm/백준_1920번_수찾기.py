import sys
input = sys.stdin.readline
N = int(input())

def binary_search(arr, f_num, start, end):
    if start <= end:
        mid = (start + end)//2
        if f_num < arr[mid]: return binary_search(arr,f_num, start, mid - 1)
        elif f_num > arr[mid]: return binary_search(arr,f_num, mid + 1, end)
        else: return 1
    else: return 0

arr = [*map(int,input().split())]
M = int(input())
search = [*map(int,input().split())]

arr.sort()
for f_num in search:
    print(binary_search(arr, f_num, 0, N-1))