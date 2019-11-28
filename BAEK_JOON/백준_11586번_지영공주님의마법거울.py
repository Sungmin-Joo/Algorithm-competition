import sys
input = sys.stdin.readline
arr = []
for i in range(int(input())):
    arr.append(input().rstrip())
num = int(input())
l = len(arr)
if num == 2:
    for i in range(l):
        print(arr[i][::-1])
elif num == 3:
    for i in range(l):
        print(arr[l-i-1])
else:
    for i in arr:
        print(i)