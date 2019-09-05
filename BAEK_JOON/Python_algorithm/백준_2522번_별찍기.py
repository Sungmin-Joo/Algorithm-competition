n = int(input())
for i in range(2*n - 1):
    if i <= n-1:
        for _ in range(n-i-1):
            print(' ',end='')
        for _ in range(i+1):
            print('*',end='')
        print()
    else:
        for _ in range(i-n+1):
            print(' ',end='')
        for _ in range(n-(i-n+1)):
            print('*',end='')
        print()