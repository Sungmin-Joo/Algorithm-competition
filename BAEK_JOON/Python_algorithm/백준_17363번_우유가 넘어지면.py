n,m=map(int,input().split())
a=[]
for i in range(n):
    buf = str(input())
    a.append([])
    for j in buf:
        if(j == '-'):
            a[i].append('|')
        elif(j == '|'):
            a[i].append('-')
        elif(j == '/'):
            a[i].append('\\')
        elif(j == '\\'):
            a[i].append('/')
        elif(j == '^'):
            a[i].append('<')
        elif(j == '<'):
            a[i].append('v')
        elif(j == 'v'):
            a[i].append('>')
        elif(j == '>'):
            a[i].append('^')
        else:
            a[i].append(j)
            
for i in range(m):
    for j in range(n):
        print(a[j][m-1-i],end='')
    print()