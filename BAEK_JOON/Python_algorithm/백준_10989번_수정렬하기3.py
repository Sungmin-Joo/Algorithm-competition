import sys
input=sys.stdin.readline
arr = [0] * 10001
if __name__ == "__main__":
    for i in range(int(input())):
        arr[int(input())] += 1
    for i in range(1, 10001):
        print("%s\n" %i *arr[i],end = "")