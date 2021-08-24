import sys
input = sys.stdin.readline

T = int(input().rstrip())
for loop in range(T):
    n = int(input().rstrip())
    coin = list(map(int,input().split()))
    m = int(input().rstrip())
    dp = [[0] * n for _ in range(m+1)]
    
    for i in range(1,m+1):
        for k in range(n):
            if i >= coin[k]:
                dp[i][k] = sum(dp[i-coin[k]])
    print(sum(dp[m]))