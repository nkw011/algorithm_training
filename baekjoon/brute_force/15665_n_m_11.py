import sys
input = sys.stdin.readline

n,m = map(int,input().split())
inputs = list(map(int,input().split()))
inputs.sort()
arrays = set()
visited = [0] * n

def dfs(numbers,count):
    global lastArray
    if count == m:
        if str(numbers) not in arrays:
            for number in numbers:
                print(number,end=" ")
            print()
            arrays.add(str(numbers))
        return
    for i in range(n):
        if visited[i] < m:
            visited[i] += 1
            numbers.append(inputs[i])
            dfs(numbers,count +1)
            visited[i] -= 1
            numbers.pop()
            
dfs([],0)