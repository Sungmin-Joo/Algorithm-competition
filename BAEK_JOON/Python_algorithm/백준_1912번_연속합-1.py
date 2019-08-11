import sys
IN=sys.stdin.readline
IN()
arr=[*map(int,IN().split())]
if max(arr) <= 0:
    print(max(arr))
else:
    s=0
    m=0
    for _ in arr:
        s+=_
        if s<0:
            s=0
        elif s>m:
            m=s
    print(m)

