def solution(baseball):
    answer = 0
    for i in range(100,1000):
        s = str(i)
        if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            continue
        if s[0] == '0' or s[1] == '0' or s[2] == '0':
            continue
        t_flag = 1
        for num, strike, ball in baseball:
            num = str(num)
            temp_strike = 0
            temp_ball = 0
            
            for j in range(3):
                if s[j] == num[j]:
                    temp_strike += 1
                elif s[j] in num:
                    temp_ball += 1
                    
            if temp_strike != strike or temp_ball != ball:
                t_flag = 0
                break

        if t_flag:
            answer += 1
            
    return answer