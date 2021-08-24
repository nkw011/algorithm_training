# 결과가 여러개라면 사전순으로 출력하는 건지는 몰랐네....(주의)
# 문제를 끝까지 읽자!!

# 방문처리할 때 배열의 사이즈가 크다면 set을 사용하는 것도 좋음
# set은 hashable 자료형만을 사용하기 때문에 in/ not in 연산이 O(1)이다...... 이거 좀 좋은듯...

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global n,m
    q = deque()
    visited = set()
    matrix = dict()
    visited.add(n)
    q.append(n)
    while q:
        s = q.popleft()
        if s == m:
            result = []
            count = 0
            # string 연산에서 걸리는 시간을 줄이기 위해 이전 것을 기억하는 방식으로 출력했다.
            # 방문처리를 set으로 했기 때문에 이전 데이터를 기억하는 것은 dictionary로 만들었다.
            while s != n:
                result.append(matrix[s][1])
                s = matrix[s][0]
                count += 1
            for i in range(count-1,-1,-1):
                print(result[i],end="")
            print()
            return
        if s *s <= int(1e9) and (s*s) not in visited:
            visited.add(s*s)
            matrix[s*s] = (s,'*')
            q.append(s*s)
        if 2*s <= int(1e9) and (2*s) not in visited:
            visited.add(2*s)
            matrix[2*s] = (s,'+')
            q.append(2*s)
        if 0 not in visited:
            visited.add(0)
            matrix[0] = (s,'-')
            q.append(0)
        if s != 0 and 1 not in visited:
            visited.add(1)
            matrix[1] = (s,'/')
            q.append(1)
    print(-1)
    return

n,m = map(int,input().split())
if n == m:
    print(0)
else :
    bfs()