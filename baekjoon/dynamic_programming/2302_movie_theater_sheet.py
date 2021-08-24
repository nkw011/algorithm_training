# 직접 유명한 수열을 파악해야하는 경우도 있다.
import sys
input = sys.stdin.readline

dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3,41):
    dp[i] = dp[i-1] + dp[i-2]
    
n = int(input().rstrip())
m = int(input().rstrip())

if m == 0:
    print(dp[n])

else :
    vip = [int(input().rstrip()) for _ in range(m)]
    vip.sort()
    cal = []
    for i in range(m):
        if i == 0:
            cal.append(vip[i]-1)
        else :
            cal.append(vip[i]-vip[i-1]-1)
    cal.append(n-vip[m-1])
    result = 1
    for num in cal:
        result *= dp[num]
    print(result)