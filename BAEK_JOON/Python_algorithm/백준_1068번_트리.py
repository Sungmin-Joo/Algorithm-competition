import sys
input=sys.stdin.readline
arr={}
n = int(input())
input_list = [*map(int,input().split())]
d = int(input())

for n, p in enumerate(input_list):
    if arr.get(p,[]) == []:
        arr[p] = [n]
    else:
        arr[p].append(n)

def del_func(i):
    if arr.get(i,0) != 0:
        for j in arr[i]:
            del_func(j)
        del arr[i]

    for childs in arr.values():
        if d in childs:
            childs.remove(d)

del_func(d)
parents = []
child = []
for n, c in arr.items():
    if c != []:
        parents.append(n)
        for i in c:
            child.append(i)
print(len(set(child) - set(parents)))