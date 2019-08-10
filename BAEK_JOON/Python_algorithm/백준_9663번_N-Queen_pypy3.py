import sys
IN=sys.stdin.readline
n=int(IN())
cnt=0
def is_ok(r):
    global col
    for i in range(r):
        if col[i] == col[r]:
            return False
        if abs(i-r) == abs(col[i]-col[r]):
            return False
    return True

def dfs(r):
    global col, cnt
    for i in range(n):
        col[r]=i
        if is_ok(r):
            if r==n-1:
                cnt+=1
            else:
                dfs(r+1)
        else:
            col[r]=0
if(n==1):
    print(1)
else:
    for i in range(n):
        global col
        col=[0]*n
        col[0]=i
        dfs(1)
    print(cnt)
