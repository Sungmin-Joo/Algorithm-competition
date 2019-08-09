import sys
IN=sys.stdin.readline

n=int(IN())

arr=[]

for _ in range(n):
    li=list(map(int,IN().split()))
    if(_==0):
        arr.append(li)
    else:
        arr.append([])
        for i in range(_+1):
            if(i==0):
                arr[_].append(arr[_-1][0]+li[0])
            elif(i==_):
                arr[_].append(arr[_-1][_-1]+li[_])
            else:
                arr[_].append(max(arr[_-1][i-1],arr[_-1][i])+li[i])

print(max(arr[n-1]))
