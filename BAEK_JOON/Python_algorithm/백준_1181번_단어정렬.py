import sys
input=sys.stdin.readline
arr = []
if __name__ == "__main__":
    for i in range(int(input())):
        arr.append(input().rstrip())
    arr = list(set(arr))
    arr.sort(key=lambda x: (len(x), x))
    for i in arr:
        print(i)