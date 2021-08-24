# 같은 문이 여러개 있을 수도 있다는 것을 간과하였다.
# 도대체 무엇이 달랐을까? 이 것도 조건을 까다롭게 생각하지 않아서 발생한 문제이다.
# 조건문을 쓰는데 조금 더 조심하게 되었다.

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs(i, j):
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        r, c = q.popleft()
        for idx in range(4):
            dy = r + my[idx]
            dx = c + mx[idx]
            if 0 <= dy < h+2 and 0 <= dx < w+2:
                if matrix[dy][dx] == '*':
                    continue
                if not visited[dy][dx]:
                    visited[dy][dx] = 1
                    if matrix[dy][dx] == '.':
                        q.append((dy, dx))
                    elif matrix[dy][dx] == '$':
                        cnt += 1
                        q.append((dy, dx))
                    # python에서 이게 가능하다니 살짝 놀라웠다.
                    elif 'A' <= matrix[dy][dx] <= 'Z':
                        diff = ord(matrix[dy][dx]) - ord('A')
                        if not key[diff]:
                            loc[diff].append((dy, dx))
                        else:
                            q.append((dy, dx))
                    elif 'a' <= matrix[dy][dx] <= 'z':
                        diff = ord(matrix[dy][dx]) - ord('a')
                        key[diff] = 1
                        while loc[diff]:
                            ny, nx = loc[diff].popleft()
                            q.append((ny, nx))
                        q.append((dy, dx))
    return cnt


my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]


T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    matrix = [['.'] * (w+2) for _ in range(h+2)]
    for i in range(h):
        temp = list(input())
        for j in range(w):
            matrix[i+1][j+1] = temp[j]
    key = [0] * 26
    keyInput = input()
    if keyInput != '0':
        for c in keyInput:
            key[ord(c) - ord('a')] = 1

    loc = [deque() for _ in range(26)]

    for k in range(26):
        if not key[k]:
            continue
        for i in range(h+2):
            for j in range(w+2):
                if matrix[i][j] == chr(ord('A') + k):
                    matrix[i][j] = '.'
    visited = [[0] * (w+2) for _ in range(h+2)]

    print(bfs(0, 0))
