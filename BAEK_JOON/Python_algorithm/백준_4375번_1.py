import sys
while(1):
    try:
        n=int(sys.stdin.readline().rstrip('\n'))
    except:
        break
    s=1
    i=1
    while(1):
        if(s%n):
            s=(s*10)+1
            i+=1
        else:
            print(i)
            break
