import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    arr.sort(reverse=True)
    for i in range(len(arr)):
        arr[i] *= i+1
    print(max(arr))