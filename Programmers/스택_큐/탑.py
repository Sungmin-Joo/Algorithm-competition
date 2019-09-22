def solution(heights):
    answer = []
    stack = []
    for idx, val in enumerate(heights):
        if idx == 0:
            #print(0,end=' ')
            answer.append(0)
            stack.append((idx+1,val))
        else:
            while 1:
                try:
                    if stack[-1][1] > val:
                        #print(stack[-1][0],end=' ')
                        answer.append(stack[-1][0])
                        stack.append((idx+1,val))
                        break
                    else:
                        stack.pop()
                except:
                    #print(0,end=' ')
                    answer.append(0)
                    stack.append((idx+1,val))
                    break
    return answer