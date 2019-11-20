import sys
input = sys.stdin.readline

class DisjointSet():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = n

    def find(self, idx):
        while idx != self.parent[idx]: idx = self.parent[idx]
        return idx

    def union(self, a, b):
        #a, b를 입력 받았을 때 a를 기준으로 합한다!
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a

        #만약 둘다 원소가 1개인 집합일 경우 바로 위 조건문에서 "parent[b] = a"가
        #실행되기 때문에 "rank[a] += 1"구문을 통해 a집합의 갯수를 한 개 늘려준다.
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1

n, m = map(int, input().split())
obj = DisjointSet(n + 1)
for _ in range(m):
    f, a, b = map(int, input().split())
    if f:
        #a와 b가 같은 집합인지 확인.
        print("YES" if obj.find(a) == obj.find(b) else "NO")
    else:
        #a와 b를 합
        obj.union(a, b)