import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = [0]*N
for i in range(N):
	arr[i] = int(input())

class SegmentTree:
	def __init__(self,values):
		self.tree = [0 for _ in values] + values
		self.n = len(values)
		for idx in reversed(range(1,self.n)):
			self.tree[idx] = min(self.tree[2*idx],self.tree[2*idx+1])

	def findmin(self,left,right):
		self.minimum = 2148473647
		left = left + self.n - 1
		right = right + self.n -1
		while left <= right:
			if left%2:
				self.minimum = min(self.minimum,self.tree[left])
				left += 1
			left //=2
			if not right%2:
				self.minimum = min(self.minimum,self.tree[right])
				right -= 1
			right //=2
		print(self.minimum)

st = SegmentTree(arr)
for i in range(M):
	left,right = map(int,input().split())
	st.findmin(left,right)
#출처 : 백준 아이디 chad4545 분 코드
#너무 깔끔하게 짜셔서 보관하고싶었습니다!