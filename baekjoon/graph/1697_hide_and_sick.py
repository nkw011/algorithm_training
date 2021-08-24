from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

INF = int(1e9)
numbers = [INF] * 100001
visited = [0] * 100001

# 방문체크 왜 안하니... 가장 중요한 건데...
# 다시 한 번 말하지만 그래프 탐색에서 가장 중요한 것은 방문했던 곳을 재차 다시 방문하지 않기 위한 방문체크이다.
# 안하면 메모리 초과같은 것이 일어나니까 재귀를 사용하는 dfs이던지 BFS이던지 둘 다 먼저 방문체크할 자료구조를 만들고 시작하자.....
def bfs(n,k):
    global minValue,numbers
    q = deque()
    q.append(n)
    visited[n] = 1
    numbers[n] = 0
    while q:
        number = q.popleft()
        if number-1 >= 0 and not visited[number-1]:
            numbers[number-1] = min(numbers[number-1], numbers[number]+1)
            visited[number-1] = 1
            q.append(number-1)
            if number -1 == k:
                return
        if number +1 <= 100000 and not visited[number+1]:
            numbers[number+1] = min(numbers[number+1], numbers[number]+1)
            visited[number+1] = 1
            q.append(number+1)
            if number+1 == k:
                return
        if number *2 <= 100000 and not visited[2*number]:
            numbers[number*2] = min(numbers[number*2], numbers[number]+1)
            visited[number*2] = 1
            q.append(number*2)
            if number * 2 == k:
                return
bfs(n,k)
print(numbers[k])