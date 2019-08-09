import sys
IN=sys.stdin.readline
n=1000-int(IN())
cnt=0
for i in [500,100,50,10,5,1]:
    if n//i:
        cnt+=n//i
        n%=i
print(cnt)
