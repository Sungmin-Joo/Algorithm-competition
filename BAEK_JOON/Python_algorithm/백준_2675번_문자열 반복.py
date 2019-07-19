for i in range(int(input())):
    r, s = input().split()
    print(''.join([w*int(r) for w in s]))