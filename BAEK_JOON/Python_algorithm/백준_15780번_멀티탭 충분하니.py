n,k=map(int,input().split())
A=map(int,input().split())
t=0
for i in A:
    t+=(i//2)
    if(i%2):
       t+=1
print("YES" if n<t else "NO")