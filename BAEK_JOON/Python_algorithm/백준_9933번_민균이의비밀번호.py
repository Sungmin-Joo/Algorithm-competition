import sys
input=sys.stdin.readline
arr = []
for i in range(int(input())):
    s = input().rstrip()
    s_r = ''.join(reversed(s))
    if s_r in arr or s == s_r:
        print(len(s))
        print(s[len(s)//2])
        break
    arr.append(s)