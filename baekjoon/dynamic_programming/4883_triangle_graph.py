# 문제를 대충 훑어 보지 말고 끝까지 잘 지켜보자 
# 문제 안 읽은 것 때문에 도대체 무슨 고생이냐...
# 조금 고쳐도 잘 안되면 처음부터 내 아이디어를 가지고 찬찬히 다시 써보는 것이 도움이 된다.

import sys
input = sys.stdin.readline

loop = 0
while True:
    loop += 1
    n = int(input().rstrip())
    if n == 0: break
    matrix = [list(map(int,input().split())) for _ in range(n)]
    dp = matrix[:]
    
    dp[1][0] = matrix[1][0] + matrix[0][1]
    dp[1][1] = min(dp[1][0],matrix[0][1],matrix[0][1] + matrix[0][2]) + matrix[1][1]
    dp[1][2] = min(dp[1][1],matrix[0][1],matrix[0][1] + matrix[0][2]) + matrix[1][2]

    for i in range(2,n):
        dp[i][0] = min(dp[i-1][0],dp[i-1][1]) + matrix[i][0]
        dp[i][1] = min(dp[i][0],dp[i-1][0],dp[i-1][1],dp[i-1][2]) + matrix[i][1]
        dp[i][2] = min(dp[i][1],dp[i-1][1],dp[i-1][2]) + matrix[i][2]
    
    print("{0}. {1}".format(loop,dp[n-1][1]))