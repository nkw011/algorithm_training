# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-1941
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-1941/

import sys
from collections import deque
from itertools import combinations, chain
def input(): return sys.stdin.readline().rstrip()

def check(case):
    my = [1,-1,0,0]
    mx = [0,0,1,-1]
    visited = set(case[1:])
    q = deque([case[0]])
    while q:
        y, x = q.popleft()
        for idx in range(4):
            dy, dx = y + my[idx], x + mx[idx]
            if dy < 0 or dx >= 5 or dx < 0 or dx >= 5: continue
            if (dy, dx) in visited:
                visited.remove((dy,dx))
                q.append((dy,dx))
    if visited:
        return False
    return True

matrix = [ list(input()) for _ in range(5)]
nums = [s for i, s in enumerate(chain(*matrix))]
location = {5 * i + j: (i, j) for i in range(5) for j in range(5)}

result = 0
for array in combinations(range(25), 7):
    count = sum(map(lambda x: 1 if nums[x] == 'S' else 0, array))
    if count >= 4 and check(list(map(lambda x: location[x], array))):
        result += 1
print(result)
