import sys
IN=sys.stdin.readline
n=int(IN())
dp={1:0,2:1,3:1}

def f_c(i):
    if i in dp.keys():
        return dp[i]
    
    if i%6==0:
        tmp = min(f_c(i//3),f_c(i//2)) + 1
    elif i%3==0:
        tmp = min(f_c(i//3),f_c(i-1)) + 1
    elif i%2==0:
        tmp = min(f_c(i//2),f_c(i-1)) + 1
    elif i>1:
        tmp = f_c(i-1)+1
    dp[i]=tmp
    return dp[i]  
print(f_c(n))
