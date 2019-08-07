import sys
n,m=map(int,sys.stdin.readline().split())
arr=[]
arr.append([0 for i in range(m+1)])
d=[]
d.append([0]*(m+1))
for i in range(1,n+1):
    arr.append([0] + list(map(int,sys.stdin.readline().split())))
    d.append([0]*(m+1))
    for j in range(1,m+1):
        d[i][j]=d[i][j-1]+d[i-1][j]-d[i-1][j-1]+arr[i][j]

n=int(input())
for z in range(n):
    i,j,x,y=map(int,input().split())
    print(d[x][y]-d[i-1][y]-d[x][j-1]+d[i-1][j-1])