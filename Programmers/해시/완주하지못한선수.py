def solution(participant, completion):
    name = {}
    answer = ''
    for i in participant:
        name[i] = name.get(i,0) + 1
    for i in completion:
        name[i] -= 1
    for k, v in name.items():
        if v != 0:
            answer = k

    return answer