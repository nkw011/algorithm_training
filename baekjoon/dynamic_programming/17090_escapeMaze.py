import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(150000)


def escape(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 1
    # 왜 무한루프가 발생하지 않냐면 다시 재차 방문한 경우 이미 dp[i][j] = 0 이라서
    # 이 조건문에 해당되어 return되기 때문이다.
    if dp[i][j] != -1:
        return dp[i][j]
    # 초기화는 0으로 나갈 수 있으면 1로 바꾼다.
    # 이런식으로 하기 때문에 무한루프가 돌지 않는다.
    dp[i][j] = 0
    if matrix[i][j] == 'U':
        dp[i][j] = max(dp[i][j], escape(i-1, j))
    elif matrix[i][j] == 'R':
        dp[i][j] = max(dp[i][j], escape(i, j+1))
    elif matrix[i][j] == 'D':
        dp[i][j] = max(dp[i][j], escape(i+1, j))
    else:
        dp[i][j] = max(dp[i][j], escape(i, j-1))
    return dp[i][j]


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# 초기화를 -1로 잘해놓은 것 같다.
dp = [[-1] * m for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if escape(i, j):
            cnt += 1
print(cnt)