import sys
input = sys.stdin.readline

n,m = map(int,input().split())
overlap = [0] * n

def dfs(numbers,last,count):
    if count == m:
        for number in numbers:
            print(number,end=" ")
        print()
        return
    
    for i in range(n):
        if i+1 >= last and overlap[i] < m:
            overlap[i] += 1
            numbers.append(i+1)
            dfs(numbers,i+1,count+1)
            numbers.pop()
            overlap[i] -= 1
            
dfs([],0,0)