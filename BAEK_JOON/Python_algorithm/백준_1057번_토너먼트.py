n,k,l=map(int,input().split())
cnt=1
while 1:
    if k%2==0 and k-l == 1:
        break
    elif l%2==0 and l-k == 1:
        break
    else:
        k = k//2 if k%2==0 else k//2 + 1
        l = l//2 if l%2==0 else l//2 + 1
        cnt+=1
print(cnt)