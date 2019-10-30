def self_num(num):
	s = num
	while num != 0:
		s += num % 10
		num //= 10
	return s

arr = [True for i in range(1,11000)]
for i in range(1,10000):
	arr[self_num(i)] = False
for i in range(1,10000):
    if arr[i] : print(i)

