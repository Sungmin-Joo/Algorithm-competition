input()
arr = input()
L_cnt = 0
cnt = len(arr)
for i in arr:
    if i == 'L': L_cnt += 1
print(cnt if L_cnt == 0 else cnt - L_cnt//2 + 1)