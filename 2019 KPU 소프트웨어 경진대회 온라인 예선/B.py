n = int(input())
arr = input()
low_arr = []
low_arr.append(arr)
for i in range(0,n):
    for j in range(i+1, n):
        low_arr.append(arr[i:j])
        low_arr.append(arr[j:])
print(low_arr)
low_arr = list(set(low_arr))
print(low_arr)
print(arr.count("bb"))