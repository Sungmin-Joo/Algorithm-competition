n = int(input())
arr = [*map(int, input().split())]
visit = [0] * (n + 1)
pivot = 1
temp_arr = []
cnt = 0
answer = []
def print_arr(arr):
    l = len(arr)
    for i, v in enumerate(arr):
        if i == l - 1:
            print(v, end = "")
        else:
            print(v, end = " ")
    print()

def find_arr(pivot):
    if not visit[pivot]:
        visit[pivot] = 1
        if pivot != arr[pivot - 1]:
            pivot = arr[pivot - 1]
            temp_arr.append(pivot)
            find_arr(pivot)
        else:
            temp_arr.append(pivot)

while sum(visit) != n:
    temp_arr = [pivot]
    find_arr(pivot)
    answer.append(temp_arr)
    for i, v in enumerate(visit):
        if i > 0 and v == 0:
            pivot =i
            break
print(len(answer))
for arr_ in answer:
    print_arr(arr_)