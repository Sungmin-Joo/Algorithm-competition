import sys
input=sys.stdin.readline
M=int(input())
N=int(input())
arr = [i*i for i in range(101) if M<=i*i<=N]
m=-1;s=0;fs=1
for i in range(M,N+1):
    if i in arr:
        if fs:
            m=i
            fs=0
        s+=i
if m==-1:
    print(-1)
else:
    print(s)
    print(m)