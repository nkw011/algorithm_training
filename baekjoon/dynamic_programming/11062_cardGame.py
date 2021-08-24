import sys
input = lambda : sys.stdin.readline().rstrip()
INF = -int(1e8)

# 이것도 전형적인 min max 알고리즘 같은데 왜 다른지...?
# 왜 이것만 시간초과가 나올까?
def cardGame(l,r,turn):
    if l > r : return 0
    if dp[l][r][turn] != -1 : return dp[l][r][turn]
    dp[l][r][turn] = INF
    dp[l][r][turn] = max(dp[l][r][turn],score[l]-cardGame(l+1,r,1- turn))
    dp[l][r][turn] = max(dp[l][r][turn],score[r]-cardGame(l,r-1,1- turn))
    return dp[l][r][turn]

# 같은 방식으로 구현한 것 같은데 차이점이 무엇일까?
def cardGame2(l,r,turn):
    if l >= r:
        if not turn : return score[l]
        else : return 0
    if dp[l][r][turn] != -1: return dp[l][r][turn]
    if not turn:
        dp[l][r][turn] = max(score[l] + cardGame2(l+1,r,1-turn),score[r] + cardGame2(l,r-1,1-turn))
    else :
        dp[l][r][turn] = min(cardGame2(l+1,r,1-turn),cardGame2(l,r-1,1-turn))
    return dp[l][r][turn]

T = int(input())
for _ in range(T):
    n = int(input())
    score = list(map(int,input().split()))
    dp = [[[-1,-1] for _ in range(n)] for _ in range(n)]
    print(cardGame2(0,n-1,0))