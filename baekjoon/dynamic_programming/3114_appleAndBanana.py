# 순방향이 안된다면 역방향으로 계산하면 된다.
# 주로 종만북에서도 역방향으로 계산을 많이 한다.

import sys
def input(): return sys.stdin.readline().rstrip()


r, c = map(int, input().split())
matrix = [list(input().split()) for _ in range(r)]

apple = [[0] * c for _ in range(r)]
banana = [[0] * c for _ in range(r)]

dp = [[-1] * c for _ in range(r)]

# 바나나 갯수 세기
for i in range(1, r):
    for j in range(c):
        banana[i][j] = banana[i-1][j]
        if matrix[i-1][j][0] == 'B':
            banana[i][j] += int(matrix[i-1][j][1:])

# 사과 갯수 세기
for i in range(r-2, -1, -1):
    for j in range(c):
        apple[i][j] = apple[i+1][j]
        if matrix[i+1][j][0] == 'A':
            apple[i][j] += int(matrix[i+1][j][1:])

dp[0][0] = apple[0][0]

for i in range(r):
    for j in range(c):
        if i-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] - apple[i-1][j] + apple[i][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + banana[i][j] + apple[i][j])
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + banana[i][j] + apple[i][j])


print(dp[r-1][c-1])
