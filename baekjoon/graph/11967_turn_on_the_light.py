# 1차로 틀린 것 : 새로 불이 켜진 방에 대한 탐색이 이루어지지 않았기 때문에 틀렸다.
# 1차 해결방안 : 만약 새로 켜진 방이 발견된다면 visted를 다시 초기화해준다.
# 2차로 틀린 것 : 불이 켜진 방의 중복체크를 하지 않음 
# 2차 해결방안 : 방을 중복 체크 하지 않도록 not light[r][c]인 곳만 불을 새로 켜주고 count 처리를 하였다.

# 이번에도 테스트 코드를 작성해서 미흡한 부분을 풀었다.
# 특히 2차로 틀린 것을 찾는데에는 테스트 코드를 작성해서 푸는 것이 도움이 되었다.
# 종종 풀리지 않는 경우가 있다면 이런식으로 테스트 코드를 작성해서 풀어봐야겠다.
# 테스트 코드 소스코드는 너무 기분이 좋은 나머지 그만 창을 닫아 버려서 날라갔다.

import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs():
    q = deque()
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    count = 1
    for r,c in matrix[0][0]:
        if not light[r][c]:
            light[r][c] = 1
            count += 1
    q.append((0,0))
    while q:
        i,j = q.popleft()
        possible = False
        for index in range(4):
            dx,dy = j + mx[index], i+my[index]
            if 0 <= dy < n and 0 <= dx < n:
                if not visited[dy][dx] and light[dy][dx]:
                    visited[dy][dx] = 1
                    for r,c in matrix[dy][dx]:
                        if not light[r][c]:
                            possible = True
                            light[r][c] = 1
                            count += 1
                    q.append((dy,dx))
        if possible:
            visited = [[0]* n for _ in range(n)]
    return count

n,m = map(int,input().split())
light = [[0]* n for _ in range(n)]
mx,my = [1,-1,0,0], [0,0,1,-1]
matrix = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c,d = map(int,input().split())
    matrix[a-1][b-1].append((c-1,d-1))
light[0][0] = 1
print(bfs())