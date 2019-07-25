a=int(input())
b=a//10
c=a%10
if(a<11):
    if a==4 or a==7:
        print(-1)
    else:
        print(2 if a==10 else a//3)
elif(c==0):
    print(b*2)
else:
    if c==7 or c==9:
        print(2*b+3)
    else:
        print(2*b+1 if c%2==1 else 2*b+2)