# 많은 걸 배운 문제이다.

# (6,13)이 나타난다는 것은 6이 13보다 높다는 뜻이 아니라 6과 13의 상대적인 순위가 바뀌었다는 뜻이다.
# 즉 항상 6이 13보다 높다는 뜻이 아니다.
# 즉 이전 순위가 13 6 이었으면 이번에는 6 13이고
# 이전 순위가 6 13이었으면 이번에는 13 6 이라는 것이다.

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def topology():
    q = deque()
    count = 0
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            count += 1
    if count > 1:
        print('?')
        return 0
    if count == 0:
        print("IMPOSSIBLE")
        return 0
    size = count
    for it in range(n):
        w = q.popleft()
        stack.append(w)
        size -= 1
        count = 0
        for i in range(1, n+1):
            if rank[w][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                    count += 1
        if count > 1:
            print('?')
            return 0
        size += count
        if it != n-1 and size == 0:
            print("IMPOSSIBLE")
            return 0
    return 1


T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    rank = [[0] * (n+1) for _ in range(n+1)]

    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1, n):
            rank[nums[i]][nums[j]] = 1
            indegree[nums[j]] += 1

    m = int(input())
    possible = True
    for _ in range(m):
        a, b = map(int, input().split())
        if rank[b][a]:
            indegree[a] -= 1
            rank[b][a] = 0
            rank[a][b] = 1
            indegree[b] += 1
        elif rank[a][b]:
            indegree[b] -= 1
            rank[a][b] = 1
            rank[b][a] = 1
            indegree[a] += 1
        else:
            possible = False

    if possible:
        stack = []
        if topology():
            for nxt in stack:
                print(nxt, end=' ')
            print()
    else:
        print("IMPOSSIBLE")
