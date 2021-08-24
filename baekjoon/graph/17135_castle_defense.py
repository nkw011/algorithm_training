# 같은 적이 여러 궁수에게 공격당할 수 있다. 라는 조건을 빼먹었다.
# 2차원 배열을 깊은 복사할 때 안에 있는 배열을 모두 깊은 복사를 해주어야 진짜 깊은 복사가 된다.

import sys
input = lambda : sys.stdin.readline()
from itertools import combinations

def simul(case,enemys):
    global maxResult, enemyCount
    kill = 0
    remain = enemyCount
    while remain > 0:
        killed  = set()
        for c in case:
            minD = 16**3
            left,loc = m, 0  
            for e in range(enemyCount):
                if not visited[e]:
                    dist = n - enemys[e][0] + abs(c-enemys[e][1]) 
                    if dist <= d:
                        if dist < minD:
                            minD,left = dist,enemys[e][1]
                            loc = e
                        elif dist == minD:
                            if left > enemys[e][1]:
                                left = enemys[e][1]
                                loc = e
            if minD != 16**3:
                killed.add(loc)
        kill += len(killed)
        remain -= len(killed)
        for num in killed:
            visited[num] = 1
        for e in range(enemyCount):
            if not visited[e]:
                enemys[e][0] += 1
                if enemys[e][0] >= n:
                    visited[e] = 1
                    remain -= 1
    if maxResult < kill:
        maxResult = kill

n,m,d = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
maxResult = 0
enemy = []
enemyCount = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            enemy.append([i,j])
            enemyCount += 1

enemy.sort(key=lambda x:(-x[0],x[1]))
visited = [0] * enemyCount
cases = list(combinations(list(range(m)),3))
for case in cases:
    temp = []
    for array in enemy:
        temp.append(array[:])
    visited = [0] * enemyCount
    simul(case,temp)
print(maxResult)