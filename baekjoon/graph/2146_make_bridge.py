# 1차 제출 - 메모리 초과
# 1차 제출 실패 이유: 길이를 넣는 배열을 2차원 배열로 만들었는데 최대 크기가 10000^2이므로 1억개 이상이 되어서 메모리 초과가 일어남
# 개선 결과 : 길이를 넣는 배열을 1차원 배열로 만들어서 구하였다.
# 또한 조합적 탐색이기 때문에 a와 b사이의 길이는 b와 a사이의 길이랑 똑같기 때문에 이 점을 이용해서 구하기도 하였다.

import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
INF = 100*100

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
island = []
mx,my = [1,-1,0,0],[0,0,1,-1] 

count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            count += 1
            q = deque()
            visited[i][j] = count
            temp = [(i,j)]
            q.append((i,j))
            while q:
                r,c = q.popleft()
                for index in range(4):
                    dx,dy = c+mx[index],r+my[index]
                    if 0 <= dy < n and 0 <= dx < n:
                        if not visited[dy][dx] and matrix[dy][dx] == matrix[i][j]:
                            visited[dy][dx] = count
                            temp.append((dy,dx))
                            q.append((dy,dx))
            island.append(temp[:])

minResult = 100*100
for i in range(count):
    for j in range(i+1,count):
        for r1,c1 in island[i]:
            for r2,c2 in island[j]:
                minResult = min(minResult,abs(r1-r2)+abs(c1-c2)-1)
print(minResult)