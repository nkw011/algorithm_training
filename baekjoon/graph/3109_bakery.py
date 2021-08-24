import sys
input = lambda: sys.stdin.readline().rstrip()

# 너무 그래프 탐색시 탐색범위 안에 있는 것만 탐색해야한다는 기본 규칙도 까먹었나보다...
# 애초에 성공하는 길을 찾아 여러번 돌아가기 때문에 실패했을 때 그 길을 방문체크하면 어떡하냐의 고민은 필요없는 것 같다.


def dfs(i, j):
    visited[i][j] = 1
    # 이미 성공한 것을 여러번 방문하지 않기 위해서이다.
    if j == c-1: return True
    for y, x in move:
        dy = i + y
        dx = j + x
        if 0 <= dy < r and 0 <= dx < c:
            if not visited[dy][dx] and matrix[dy][dx] == '.' and dfs(dy, dx):
                return True


r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
move = [(-1, 1), (0, 1), (1, 1)]
count = 0
for i in range(r):
    if dfs(i, 0):
        count += 1
print(count)