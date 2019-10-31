def solution(numbers, target):
    answer = 0
    l = len(numbers)
    def dfs(i):
        if i < l:
            dfs(i+1)
            numbers[i] *= -1
            dfs(i+1)
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
    dfs(0)
    return answer