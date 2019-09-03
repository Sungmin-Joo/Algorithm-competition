import sys
from math import ceil, log

input = sys.stdin.readline
global arr, size, size_max

def sum(left, right, node_left, node_right, node_num):
    if left > node_right or right < node_left: return 0
    if left <= node_left and right >= node_right: return arr[node_num]

    mid = (node_left + node_right)//2
    return sum(left, right, node_left, mid, node_num*2) + sum(left, right, mid+1, node_right, node_num*2 + 1)

def modify(i, val):
    global arr
    i += size - 1
    arr[i] = val
    while i > 1:
        i //= 2
        arr[i] = arr[i*2] + arr[i*2+1]

def init():
    global size, arr
    for i in range(size - 1, 0, -1):
        arr[i] = arr[i*2] + arr[i*2 + 1]

N, M, K = map(int,input().split())

size =  2**ceil(log(N,2))
size_max = size * 2
arr = [0]*(size_max)
for i in range(N):
    arr[size+i]=int(input())
init()
for _ in range(M + K):
    flag, f, s = map(int,input().split())
    if flag == 1:
        modify(f,s)
    else:
        print(sum(f-1, s-1, 0, size - 1,1))