# https://programmers.co.kr/learn/courses/30/lessons/43162

import sys
from collections import deque
input = sys.stdin.readline 


def solution(n,computers):
    visited = [0] * n
    q = deque()
    count = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[i]:
                count += 1
                visited[i] = 1
                q.append(i)
                while q:
                    node = q.popleft()
                    for k in range(n):
                        if k != node and computers[node][k] == 1 and not visited[k]:
                            visited[k] = 1
                            q.append(k)
    return count