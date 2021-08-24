# combination을 만들어서 푸는 방법도 있기는 하다...
# 먼저 탐색을 할 때 순열 / 조합 / 부분집합 중 어떤 것으로 풀 수 있는 지 한 번 확인해보자

import sys
input = sys.stdin.readline

dwarfs = []
visited = [0] * 9
result = []
sums = 0
solution = []

for _ in range(9):
    dwarfs.append(int(input().rstrip()))
    
def dfs(dwarfs,count):
    global solution,result,sums
    if sums > 100 or count > 7:
        return 
    
    if sums == 100 and count == 7:
        solution = result[:]
        return
    
    for i in range(9):
        if not visited[i]:
            visited[i] = 1
            result.append(dwarfs[i])
            sums += dwarfs[i]
            
            dfs(dwarfs,count+1)
            
            result.pop()
            sums -= dwarfs[i]
            visited[i] = 0

dfs(dwarfs,0)
solution.sort()
for length in solution:
    print(length)