# dp top-down approach에 대해 다시 익히고 배우는 기분이다...
# 조건이 들어가있는 dp의 경우 top-down approach에 대한 문제인 경우가 많다.
# 그리고 top-down approach의 경우 초기값을 무엇으로 할 지에 대해 고민을 많이 해야할 것 같았다.
# 예를 들어서 아래의 경우 이미 방문한 결과의 경로의 수가 0일 수도 있음에도 dp[i][j] != 0 일 경우에만 return을 해주게 되어 시간 초과가 일어났다..
# 이런 경우를 생각해서 top-down 접근시 dp table을 어떤 값으로 초기화할 지 잘 생각해 보는 것이 좋을 것 같다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

h,w = map(int,input().split())
result = 0
matrix = [list(map(int,input().split())) for _ in range(h)]
dp = [[-1] * w for _ in range(h)]
dp[0][0] = 1
mx = [1,-1,0,0]
my = [0,0,1,-1]

def solution(r,c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    for index in range(4):
        dx,dy = c + mx[index], r+my[index]
        if 0 <= dy < h and 0 <= dx < w and matrix[dy][dx] > matrix[r][c]:
            if dp[r][c] == -1:
                dp[r][c] = 0
            dp[r][c] += solution(dy,dx)
            
    if dp[r][c] == -1:
        dp[r][c] = 0
    
    return dp[r][c]
    
print(solution(h-1,w-1))