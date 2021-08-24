import sys
input = sys.stdin.readline

n,s,m = map(int,input().split())
v = list(map(int,input().split()))

def dynamic():
    global n,s,m,v
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][s] = 1
    for i in range(1,n+1):
        value = v[i-1]
        nothing = True
        for j in range(m+1):
            if dp[i-1][j] != 0 :
                if j + value <= m and dp[i][j+value] == 0 :
                    dp[i][j+value] =1
                    nothing = False
                if j - value >= 0 and dp[i][j-value] == 0 :
                    dp[i][j-value] =1
                    nothing = False
        if nothing:
            print(-1)
            return
    result = -1
    for j in range(m+1):
        if dp[n][j] != 0:
            result = j
    print(result)
    
dynamic()