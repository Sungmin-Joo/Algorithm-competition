s,s2 = [list(input()) for i in range(2)]
c=0
for i in s2:
    try:
        s.remove(i)
    except:
        c +=  1     
print(c + len(s))