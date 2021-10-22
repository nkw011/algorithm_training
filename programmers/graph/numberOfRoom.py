# https://programmers.co.kr/learn/courses/30/lessons/49190
# 방이 만들어지는 경우
# 1. 방문했던 점을 다시 방문하는 경우
# 2. 기존에 갔던 edge로 다시 돌아가지 않은 경우
# 교차로 만들어지는 방을 체크하기 위해서
# 1. 칸의 크기를 늘리면 해결이 되는 것이었다...

def solution(arrows):
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)]
    visited = set()
    edge = set()
    y, x = 0, 0
    visited.add((y, x))
    cnt = 0
    for idx in arrows:
        for _ in range(2):
            dy, dx = y+move[idx][0], x+move[idx][1]
            if (dy, dx) not in visited:
                visited.add((dy, dx))
                edge.add((y, x, dy, dx))
            else:
                if (dy, dx, y, x) not in edge and (y, x, dy, dx) not in edge:
                    cnt += 1
                    edge.add((y, x, dy, dx))
            y, x = dy, dx
    return cnt
