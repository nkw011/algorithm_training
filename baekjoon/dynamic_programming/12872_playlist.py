import sys
MOD = 1000000007
def input(): return sys.stdin.readline().rstrip()


n, m, p = map(int, input().split())
dp = [[0] * (n+1) for _ in range(p+1)]

# dp[i][j]: 현재 플레이리스트의 길이가 i이고 사용한 숫자의 갯수가 j일 때 만들 수 있는 플레이리스트의 수
dp[1][1] = n
for i in range(2, p+1):
    for j in range(n+1):
        if j-1 >= 0:
            dp[i][j] = dp[i-1][j-1] * (n-j+1)
        if j > m:
            dp[i][j] += dp[i-1][j] * (j-m)
        dp[i][j] %= MOD

print(dp[p][n])
