import sys
input = sys.stdin.readline

n,m = map(int,input().split())
overlap = [0] * n

def dfs(numbers,count):
    if count == m:
        for number in numbers:
            print(number,end=" ")
        print()
        return
    
    for i in range(n):
        if overlap[i] < m:
            overlap[i] += 1
            numbers.append(i+1)
            dfs(numbers,count+1)
            numbers.pop()
            overlap[i] -= 1
            
dfs([],0)