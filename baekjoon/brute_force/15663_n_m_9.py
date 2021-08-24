import sys
input = sys.stdin.readline

n,m = map(int,input().split())
inputs = list(map(int,input().split()))
inputs.sort()
arrays = set()
visited = [0] * n
maxValue = max(inputs)



# 풀이 방법 1
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
        if not visited[i]:
            visited[i] = 1
            numbers.append(inputs[i])
            dfs(numbers,count +1)
            visited[i] = 0
            numbers.pop()

# 풀이 방법2
def dfs2(numbers,count):
    global maxValue
    if count == m:
        for number in numbers:
            print(number, end=" ")
        print()
        return
    
    used = [0] * (maxValue +1)
    for i in range(n):
        if not visited[i] and not used[inputs[i]]:
            visited[i] = 1
            used[inputs[i]] = 1
            numbers.append(inputs[i])
            dfs2(numbers,count+1)
            visited[i] = 0
            numbers.pop()
            
dfs2([],0)