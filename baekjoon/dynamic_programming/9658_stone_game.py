import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [-1,1,0,1,0,0,0]

if n <= 6:
    print("SK") if dp[n] == 0 else print("CY")
else :
    for i in range(7,n+1):
        if i == n:
            if dp[i-1] or dp[i-3] or dp[i-4]:
                print("SK")
            else :
                print("CY")
        else :
            if dp[i-1] or dp[i-3] or dp[i-4]:
                dp.append(0)
            else :
                dp.append(1)