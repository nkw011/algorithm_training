import sys
input = sys.stdin.readline

n = int(input().rstrip())
visited = [0] * n

def dfs(numbers,count):
    if count == n:
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