import sys
input = sys.stdin.readline

n,m = map(int,input().split())
inputs = list(map(int,input().split()))
inputs.sort()
visited = [0] * n

def dfs(numbers,count):
    if count == m:
        for number in numbers:
            print(number,end=" ")
        print()
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            numbers.append(inputs[i])
            dfs(numbers,count+1)
            numbers.pop()
            visited[i] = 0
            
dfs([],0)