# python으로 EOFError가 발생하기 전까지 입력을 받으러면 try-except 구문을 사용하면 될 것 같다.
# n이 0일 때의 방법은 아무것도 하지 않는다는 방법이 있으므로 dp[0] = 1이다.

import sys
input = lambda : sys.stdin.readline()

dp = [0] * 251
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3,251):
    dp[i] = dp[i-1] + dp[i-2] * 2
    
while True:
    try:
        n = int(input())
        print(dp[n])
    except: break