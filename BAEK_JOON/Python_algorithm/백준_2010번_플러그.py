import sys
IN=sys.stdin.readline
cnt=1
for _ in range(int(IN())):
    cnt+=int(IN())-1
print(cnt)