import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int,input().split()))
visited = [0] * n
maxValue = 0

def dfs(numbers,count):
    global maxValue
    if count == n:
        value = 0
        for i in range(1,n):
            value += abs(numbers[i] - numbers[i-1])
        maxValue = max(maxValue,value)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            numbers.append(nums[i])
            dfs(numbers,count+1)
            numbers.pop()
            visited[i] = 0
            
dfs([],0)
print(maxValue)