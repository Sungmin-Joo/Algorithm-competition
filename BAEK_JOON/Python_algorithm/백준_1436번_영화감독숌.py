n = int(input())
num = 665
while n:
    num += 1
    if "666" in str(num):
        n -= 1
        continue
print(num)