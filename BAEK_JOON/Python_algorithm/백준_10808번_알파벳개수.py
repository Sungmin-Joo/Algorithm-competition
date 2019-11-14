arr = [0]*26
for i in input():
    arr[ord(i)-97] += 1
print(' '.join([*map(str,arr)]))