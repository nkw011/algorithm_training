import sys
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if dp[i][j]:
            dist = matrix[i][j]
            if i + dist < n:
                dp[i+dist][j] += dp[i][j]
            if j + dist < n :
                dp[i][j+dist] += dp[i][j]
print(dp[n-1][n-1])

# q와 visited를 활용한 답안에서는 다 더하지도 않았는데 미리 넘어가서 다음 경로를 가는 문제가 발생해서
# 값이 여러번 더해지는 문제가 발생했다.. 이에 따라 이 문제를 해결하기 위해
# 매트릭스의 전체를 훑으면서 값이 0이 아닌 부분에 대해 경로를 진행하는 방식으로 하니
# 문제가 바로 해결이 되었다
# 가장 짧은 경로를 찾는 것도 아니고 모든 경로를 찾는 것이기 때문에 bfs를 활용한 방식은 조금은 무리였다고 생각한다.
# 이 문제는 역시 dp문제 였던 것이다.