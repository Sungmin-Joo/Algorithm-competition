import sys
input=sys.stdin.readline


if __name__ == "__main__":
    n = (int(input())//100) * 100
    f = int(input())
    i = 0
    while (n + i) % f:
        i += 1

    if i < 10:
        print('0',end = '')
    print(i)