n,T=map(int,input().split())
c=[]
for i in map(int,input().split()):
    T-=i
    c.append(1 if(T>0) else 0)
print(sum(c))