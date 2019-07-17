[a, b] = input().split(' ')
for w in a:
    if(w in b):
        i = b.find(w)
        j = a.find(w)
        break
for z in range(len(b)):
    if(i == z):
        print(a)
    else:
        print('.'*j + b[z] +'.'*(len(a) - j - 1))