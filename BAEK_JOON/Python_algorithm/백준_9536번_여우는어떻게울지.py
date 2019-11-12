import sys
input=sys.stdin.readline

for _ in range(int(input())):
    string = input().split()
    while 1:
        s = input().split()
        if s[0] == 'what': break
        for i in range(len(string)):
            if string[i] == s[2] : string[i]=''

    print(' '.join(i for i in string if i != ''))