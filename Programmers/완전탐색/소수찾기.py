from itertools import permutations
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return sieve
    #출처 : 위키피디아 - https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

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