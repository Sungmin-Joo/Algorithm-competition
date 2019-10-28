def fact_mod(n):
    s = 1
    for i in range(2, n + 1):
        s = s * i % p
    return s
n, p = map(int, input().split())
if n == p - 1 or n == 1: print(n)
elif n == p - 2: print(1)
else: print(fact_mod(n))