def solution(budgets, M):
    answer = 0
    budgets.sort(reverse = True)
    high = budgets[0]
    low = 0
    if sum(budgets) < M:
        return budgets[0]
    else:
        while low < high:
            mid = (high + low)//2
            money = M
            for budget in budgets:
                if budget > mid:
                    money -= mid
                else:
                    money -= budget
                if money < 0:
                    break
            if money < 0:
                high = mid
            else:
                low = mid + 1
                answer = mid
          
    return answer