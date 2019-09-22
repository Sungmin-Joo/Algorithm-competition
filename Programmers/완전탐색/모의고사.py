def solution(answers):
    arr = [[(1,2,3,4,5), 0], [(2,1,2,3,2,4,2,5), 0], [(3,3,1,1,2,2,4,4,5,5), 0]]
    
    for idx, val in enumerate(answers):
        if arr[0][0][idx % 5] == val:
            arr[0][1] += 1
        if arr[1][0][idx % 8] == val:
            arr[1][1] += 1
        if arr[2][0][idx % 10] == val:
            arr[2][1] += 1
    answer = []
    m = max(arr[0][1], arr[1][1], arr[2][1])
    for i in range(3):
        if m == arr[i][1]:
            answer.append(i+1)
    return answer