import sys
input = sys.stdin.readline

def dfs(cases,index,count):
    if count == 6:
        for case in cases:
            print(case, end=" ")
        print()
        return
    for i in range(index+1,n+1):
        if not visited[i]:
            visited[i] = 1
            cases.append(numbers[i])
            dfs(cases,i,count+1)
            cases.pop()
            visited[i] = 0


while True:
    numbers = list(map(int,input().split()))
    if numbers[0] == 0:
        break
    n = numbers[0]
    visited = [0] * (n+1)
    dfs([],0,0)
    print()