string, boom = input(), list(input())
l = len(boom)
answer = []

for c in string:
    answer.append(c)
    if answer[-l:] == boom:
        answer[-l:] = []
print(''.join(answer) if answer else "FRULA")