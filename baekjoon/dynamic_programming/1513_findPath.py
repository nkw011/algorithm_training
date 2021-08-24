import sys
MOD = 1000007
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(100000)


# 왜 dp에 num이 필요할까? 생각해봤는데.. // 괜히 parameter로 들어가는 것이 아니다.
# 숫자가 커지게되면 현재 숫자랑 cnt를 반영한 것이 조금 달라지기 때문이다. 
# 즉 항상 cnt가 일정하게 되지 않고... num에 따라 cnt 측정갯수가 달라지기 때문에 dp에 num을 추가한 것이 필요하다.
def findPath(i, j, num, count):
    if i == n and j == m:
        if count == 0:
            return 1
        return 0
    if dp[i][j][num][count] != -1:
        return dp[i][j][num][count]
    dp[i][j][num][count] = 0
    if i + 1 <= n:
        if matrix[i+1][j] == 0:
            dp[i][j][num][count] += findPath(i+1, j, num, count)
        elif matrix[i+1][j] > num:
            dp[i][j][num][count] += findPath(i+1, j, matrix[i+1][j], count-1)
        dp[i][j][num][count] %= MOD
    if j+1 <= m:
        if matrix[i][j+1] == 0:
            dp[i][j][num][count] += findPath(i, j+1, num, count)
        elif matrix[i][j+1] > num:
            dp[i][j][num][count] += findPath(i, j+1, matrix[i][j+1], count-1)
        dp[i][j][num][count] %= MOD

    return dp[i][j][num][count]


n, m, c = map(int, input().split())
matrix = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, c+1):
    a, b = map(int, input().split())
    matrix[a][b] = i

dp = [[[[-1] * (c+1) for _ in range(c+1)] for _ in range(m+1)]
      for _ in range(n+1)]

for cnt in range(c+1):
    if matrix[1][1] == 0:
        print(findPath(1, 1, matrix[1][1], cnt), end=' ')
    else:
        if cnt-1 < 0:
            print(0, end=' ')
        else:
            print(findPath(1, 1, matrix[1][1], cnt-1), end=' ')
print()
