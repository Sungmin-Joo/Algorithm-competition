import sys
input = sys.stdin.readline

def prime_list(n, k):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(2, n + 1):
        if sieve[i] == True: # i가 소수인 경우
            for j in range(i, n + 1, i): # i이후 i의 배수들을 False 판정
                if sieve[j] == True:
                    sieve[j] = False
                    k-=1
                    if k == 0:
                        print(j)
                        return

    # 소수 목록 산출
    return(sieve)
    #출처 : 위키백과 https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
n, k = map(int,input().split())
print(prime_list(n,k))