import sys
input = sys.stdin.readline

d = {}

n = int(input())
cnt = n
for _ in range(n):
    s = input().rstrip()
    d.clear()
    check = s[0]
    for char in s:
        if d.get(char,None) != None:
            if char != check:
                cnt-=1
                break
        else:
            d[char] = 1
        check = char
print(cnt)