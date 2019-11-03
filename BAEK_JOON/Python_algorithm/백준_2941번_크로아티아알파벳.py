arr = input()
sub_arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for ch in sub_arr:
    arr = arr.replace(ch,'?')
print(len(arr))
