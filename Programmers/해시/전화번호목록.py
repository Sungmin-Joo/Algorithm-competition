def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : len(x))
    l = len(phone_book)
    f_flag = 0
    for i in range(l):
        for j in range(i+1, l):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                f_flag = 1
                break
        if f_flag:
            break
    answer = False if f_flag else True
            
    return answer