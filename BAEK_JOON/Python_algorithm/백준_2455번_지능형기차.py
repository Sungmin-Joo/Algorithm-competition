import sys
input = sys.stdin.readline
t_c, m = 0, 0
for i in range(1,5):
    i_c, o_c = map(int,input().split())
    t_c = t_c - i_c + o_c
    if t_c > m:
        m = t_c
print(m)