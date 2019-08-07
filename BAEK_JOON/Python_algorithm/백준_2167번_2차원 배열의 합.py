import sys
IN=sys.stdin.readline
n,m=map(int,IN().split())
arr=[[0]*-~m]
for i in range(n):
    arr.append([0] + list(map(int,IN().split())))
for i in range(1,n+1):
    w=arr[i-1]
    for j in range(1,m+1):
        arr[i][j]+=w[j]+arr[i][j-1]-w[j-1]

for z in range(int(input())):
    i,j,x,y=map(int,IN().split())
    print(arr[x][y]-arr[i-1][y]-arr[x][j-1]+arr[i-1][j-1])