import sys
IN=sys.stdin.readline
n=int(IN())
arr=[]
buf=0
for _ in list(map(int,IN().split())):
    if(_>0):
        buf+=_
    else:
        if(buf):
            arr.append(buf)
            buf=0
        arr.append(_)
if(buf):
    arr.append(buf)

m=-1000
n=len(arr)
dp=[0]*n
dp[n-1]=arr[n-1]
for i in range(n-2,-1,-1):
    dp[i]=max(arr[i],arr[i]+dp[i+1])
for i in dp:
    if i>m:
        m=i
print(m)   
