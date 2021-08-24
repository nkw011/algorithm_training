# dp를 (x,y)까지 가는데 최대 거리가 아니라 (x,y)로부터 얼마나 멀리 갈 수 있는지를 고민하니까 풀 수 있었다.
# 정말 집중적으로 종만북을 통해 공부를 해야겠다는 생각이 든다.
# 재귀 깊이가 깊어 200000으로 해야 recursion Error가 나오지 않았다.

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(200000)

def solution(i,j):
    if dp[i][j] !=0:
        return dp[i][j]
    for index in range(4):
        dx,dy = j+mx[index],i+my[index]
        if 0 <= dy < n and 0 <= dx < n:
            if matrix[dy][dx] > matrix[i][j]:
                temp = 1
                temp += solution(dy,dx)
                dp[i][j] = max(dp[i][j],temp)
    if dp[i][j] == 0:
        dp[i][j] = 1
    return dp[i][j]

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
mx = [1,-1,0,0]
my = [0,0,1,-1]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        solution(i,j)

maxResult = 0
for i in range(n):
    for j in range(n):
        maxResult = max(maxResult,dp[i][j])
print(maxResult)