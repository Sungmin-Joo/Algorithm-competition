import sys
input = sys.stdin.readline

def solution(arr):
    result = [0,[]]
    for k, v in arr.items():
        if v == 2:
            result[0] += 1
            result[1].append(k)

    result[1].sort()
    return  result


if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = {}

    for _ in range(N):
        arr[input().rstrip()] = 1

    for _ in range(M):
        name = input().rstrip()
        if arr.get(name,0) == 1:
            arr[name] = 2

    result = solution(arr)
    print(result[0])
    for name in result[1]:
        print(name)