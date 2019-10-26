import sys
input=sys.stdin.readline

if __name__ == "__main__":
    n1, n2 = input().split()
    n1, n2 = int(n1[::-1]), int(n2[::-1])
    print(max(n1, n2))

