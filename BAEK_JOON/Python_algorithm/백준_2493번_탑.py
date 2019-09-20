import sys
input = sys.stdin.readline

n = int(input())
arr = []
stack = []

for idx, val in enumerate([*map(int,input().split())]):
    if idx == 0:
        print(0,end=' ')
        stack.append((idx+1,val))
    else:
        while 1:
            try:
                if stack[-1][1] > val:
                    print(stack[-1][0],end=' ')
                    stack.append((idx+1,val))
                    break
                else:
                    stack.pop()
            except:
                print(0,end=' ')
                stack.append((idx+1,val))
                break
print()