x=int(input())
d=[64]
while 1:
    if x==64:
        break

    if sum(d) > x:
        m=min(d)
        del d[d.index(m)]
        d.append(m/2)
        if(sum(d)<x):
            d.append(m/2)
    if sum(d)==x:
        break
print(len(d))