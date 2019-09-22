import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    index = 0
    heap_lsit = []
    sup_data = list(zip(dates, supplies))
    l = len(dates)

    while stock < k:
        for i in range(index, l):
            if sup_data[i][0] <= stock:
                heapq.heappush(heap_lsit,(-sup_data[i][1]))
            else:
                break
            index += 1
        stock += -1 * heapq.heappop(heap_lsit)
        answer += 1
    return answer