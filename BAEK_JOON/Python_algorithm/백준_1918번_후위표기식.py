def check(x) :
    if x in ['*', '/']:
        return 3
    elif x in ['+', '-']:
        return 2
    elif x in ["(", ")"]:
        return 1
    return 0


s = input()
answer = ''
stack = []

for cha in s:
    pri = check(cha)
    if cha in ['+', '-', '*', '/']:
        #스택의 top보다 비교 대상 연산자의 연산자가 낮거나 같을 경우 = pop
        while stack and check(stack[-1]) >=  pri:
            answer += stack.pop()
        stack.append(cha)
    elif cha == '(':
        stack.append(cha)
    elif cha == ')':
        while stack and stack[-1] != "(" :
            answer += stack.pop()
        stack.pop()
    else:
        answer += cha
#마지막 스택에 남은 원소를 모두 결과에 삽입
while stack :
    answer += stack.pop()
print(answer)
