def solution(record):
    answer = []
    in_out_list = []
    id_list = {}
    for string in record:
        temp = list(string.split())
        if temp[0] == "Enter":
            id_list[temp[1]] = temp[2]
            in_out_list.append([1,temp[1]])
        elif temp[0] == "Leave":
            in_out_list.append([0,temp[1]])
        else:
            id_list[temp[1]] = temp[2]
    for flag, id in in_out_list:
        if flag:
            answer.append(str(id_list[id] + "���� ���Խ��ϴ�."))
        else:
            answer.append(str(id_list[id] + "���� �������ϴ�."))
    return answer