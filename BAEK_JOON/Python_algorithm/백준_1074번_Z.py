import math
N,r,c=map(int,input().split())
cnt=0
for i in range(N,0,-1):
    n=int(math.pow(2,i))//2
    t_r=r//n
    t_c=c//n
    if t_r==0 and t_c == 0:
        lo=0
    elif t_r==0 and t_c == 1:
        lo=1
    elif t_r==1 and t_c == 0:
        lo=2
    else:
        lo=3
    cnt+=math.pow(n,2)*lo
    r=r%n
    c=c%n
print(int(cnt))
