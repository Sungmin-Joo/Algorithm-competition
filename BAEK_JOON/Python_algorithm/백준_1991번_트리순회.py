import sys
IN=sys.stdin.readline
data={}

def tr(d,k,m):
    if(m==0):
        print(k,end='')
    if(d[k][0] != '.'):
        tr(d,d[k][0],m)
    if(m==1):
        print(k,end='')
    if(d[k][1] != '.'):
        tr(d,d[k][1],m)
    if(m==2):
        print(k,end='')
    
for _ in range(int(IN())):
    arr=list(IN().split())
    data[arr[0]]=arr[1:]

tr(data,'A',0)
print()
tr(data,'A',1)
print()
tr(data,'A',2)
