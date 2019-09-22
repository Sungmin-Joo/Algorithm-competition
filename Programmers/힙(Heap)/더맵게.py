import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if K == 0:
        return 0
    l = len(scoville)
    if l == 0 or l == 1:
        return -1
        
    if scoville[0] == 0:
        temp = heapq.heappop(scoville)
        if scoville[0] == 0:
            return -1
        else:
            heapq.heappush(scoville,0)
    while scoville[0] < K:
        if l == 0 or l == 1:
            return -1
        n_1, n_2 = heapq.heappop(scoville), heapq.heappop(scoville)
        n_1 += n_2*2
        heapq.heappush(scoville,n_1)
        answer += 1
        l -= 1
    print(scoville)
    return answer