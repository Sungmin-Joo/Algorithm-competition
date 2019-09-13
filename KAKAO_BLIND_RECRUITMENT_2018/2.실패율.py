def solution(N, stages):
    answer = []
    stage_list = [0]*(N+1)
    dp = [0]*(N)
    ratio = {}
    
    for i in stages:
        stage_list[i-1] += 1

    for i in range(N-1,-1,-1):
        if i == N-1:
            dp[i] = stage_list[i] + stage_list[-1]
        else:
            dp[i] = dp[i+1] +stage_list[i]
        ratio[i+1] = 0 if dp[i] == 0 else stage_list[i]/dp[i]
    ratio = sorted(ratio.items(), key=lambda x: x[1])
    
    for i in range(N):
        answer.append(ratio.pop()[0])
        
    return answer