import math
import sys

def update(tree,node,start,end,index,diff):
    if(index < start or index > end):
        return
    tree[node] = tree[node] + diff
    if(start != end):
        update(tree,node*2,start, int((start+end)/2),index,diff)
        update(tree,(node*2)+1,int(((start+end)/2)+1),end,index,diff)
 
def sum_num(tree,node,start,end,left,right):
    if(left > end or right < start):
        return 0
    if(left <= start and end <= right):
        return tree[node]
    return sum_num(tree, node*2, start,int((start+end)/2),left,right) +\
           sum_num(tree, node*2+1, int(((start+end)/2)+1), end, left,right)

input=sys.stdin.readline

[n, m] = input().split(' ')
n = int(n)
h = int(math.ceil(math.log(n,2)))
A = [0]*n
B = [0]*(1<<(h+1))

for i in range(int(m)):
    [k, x, v] = input().split(' ')
    x = int(x);v = int(v)
    if(int(k)):
        x -= 1
        dif = v - A[x]
        A[x] = v
        update(B,1,0,n-1,x,dif)
    else:
        if(x < v):
            print(sum_num(B, 1, 0, n-1, x-1, v-1))
        else:
            print(sum_num(B, 1, 0, n-1,v-1,x-1))