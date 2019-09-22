from itertools import permutations
def prime_list(n):
    # �����佺�׳׽��� ü �ʱ�ȭ: n�� ��ҿ� True ����(�Ҽ��� ����)
    sieve = [True] * n

    # n�� �ִ� ����� sqrt(n) �����̹Ƿ� i=sqrt(n)���� �˻�
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i�� �Ҽ��� ��� 
            for j in range(i+i, n, i): # i���� i�� ������� False ����
                sieve[j] = False

    # �Ҽ� ��� ����
    return sieve
    #��ó : ��Ű�ǵ�� - https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

def solution(numbers):
    answer = 0
    num = prime_list(9999999)

    for i in range(len(numbers)):
        for j in set(list(permutations(numbers,i+1))):
            string = int("".join(list(j)))
            if num[string] == True and string > 1:
                print(string)
                answer += 1
                num[string] = False
    #print(prime_list(9999999))
    return answer