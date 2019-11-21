s, p, k = map(int, input().split())


if k == 1:
    if s == p: print(s)
    else: print("NO")
elif k == 2:
    for i in range(1, s+1):
        for j in range(1, s+1):
            if s == i + j:
                tmp = i * j
                if p == tmp:
                    print(i, j)
                    exit(0)
                elif p < tmp:
                    break
            elif s < i + j:
                break
elif k == 3:
    for i in range(1, s+1):
        for j in range(1, s+1):
            k = s - i - j
            tmp = i * j * k 
            if p == tmp:
                print(i, j, k)
                exit(0)
elif k == 4:
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                l = s - i - j - k
                tmp = i * j * k * l
                if p == tmp:
                    print(i, j, k, l)
                    exit(0)
print("NO")

