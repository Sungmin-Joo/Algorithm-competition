from collections import deque


def solution(priorities, location):
    q = deque()
    printed_queue = []
    for idx, priority in enumerate(priorities):
        q.append((idx, priority))
        
    while q:
        data = q.popleft()
        priority = data[1]
        
        if q:
            max_priority = max(q, key = lambda x : x[1])[1]
        
        if priority < max_priority:
            q.append(data)

        else:
            printed_queue.append(data)

    cnt = 1
    for data in printed_queue:
        if data[0] == location:
            break
        cnt += 1

    return cnt