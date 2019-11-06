n = [*map(int, input())]
if not 0 in n:
    print(-1)
    exit(0)

m = 0
for num in n:
    m += num
if m % 3 == 0:
    n.sort(reverse = True)
    [print(i, end = '') for i in n]
else:
    print(-1)