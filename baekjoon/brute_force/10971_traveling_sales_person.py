import sys
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited  = [0] * n
minCost = int(1e9)

def bruteforce(numbers,count):
    global minCost
    if count == n :
        cost = 0
        for i in range(n):
            if i == n-1:
                if matrix[numbers[n-1]][numbers[0]] == 0:
                    return
                cost += matrix[numbers[n-1]][numbers[0]]
            else :
                if matrix[numbers[i]][numbers[i+1]] == 0:
                    return
                cost += matrix[numbers[i]][numbers[i+1]]
        minCost = min(cost,minCost)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            numbers.append(i)
            bruteforce(numbers,count+1)
            numbers.pop()
            visited[i] = 0
        
bruteforce([],0)
print(minCost)