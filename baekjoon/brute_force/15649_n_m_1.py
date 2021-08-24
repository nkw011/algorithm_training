import sys
input = sys.stdin.readline
import itertools

n,m = map(int,input().split())


# 순열 라이브러리를 이용한 탐색
# result = list(itertools.permutations(list(range(1,n+1)),m))
# for elem in result:
#     for i in range(m):
#         print(elem[i],end=" ")
#     print()

# 재귀를 이용한 탐색
nums = list(range(1,n+1))
visited = [0] *(n+1)

def dfs(numbers,count):
    if count == m:
        for number in numbers:
            print(number,end=" ")
        print()
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            numbers.append(i+1)
            dfs(numbers,count+1)
            numbers.pop()
            visited[i] = 0
dfs([],0)