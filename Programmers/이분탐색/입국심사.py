def solution(n, times):
    answer = []
    if len(times) == 1:
        return times[0] * n
    times.sort(reverse = True)
    low = 0
    high = times[0] * n
    answer.append(high)
    while low <= high:
        mid = (high + low)//2
        cnt = 0
        print(low,mid,high)
        for i in times:
            cnt += mid//i
            if cnt == n:
                answer.append(mid)
                break
            if cnt > n and (cnt - n) <= (mid // i):
                answer.append(mid)
                break
        if cnt >= n:
            high = mid  - 1
        else:
            low = mid + 1
     
    return min(answer)