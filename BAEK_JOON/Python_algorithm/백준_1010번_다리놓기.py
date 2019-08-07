import sys
import math
IN=sys.stdin.readline
def mem(func):
    mem={}
    def wrapper(n):
        if n in mem:
            return mem[n]
        else:
            mem[n] = func(n)
            return mem[n]
    return wrapper

@mem
def fact(n):
    return n*fact(n-1) if n > 1 else 1
#'@' => deco_func = mem(fact)
#       deco_func(n) ==> wrapper(n) ==> fact(n)
for _ in range(int(IN())):
    n,m=map(int,IN().split())
    print(fact(m)//fact(n)//fact(m-n))

#참고 : https://nachwon.github.io/decorator/
