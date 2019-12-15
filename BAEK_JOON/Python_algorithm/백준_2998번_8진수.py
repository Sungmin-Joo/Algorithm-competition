arr = input()
mod = len(arr) % 3
if mod == 0: mod = 3
arr = "0" * (3 - mod) + arr

table = {
    "000" : 0,
    "001" : 1,
    "010" : 2,
    "011" : 3,
    "100" : 4,
    "101" : 5,
    "110" : 6,
    "111" : 7,
}

for i in range(0, len(arr), 3):
    print(table[arr[i:i+3]], end = "")