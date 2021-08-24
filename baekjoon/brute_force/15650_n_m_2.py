import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [0] * (n+1)

def combination(numbers,index,count):
    if count == m:
        for number in numbers:
            print(number,end=" ")
        print()
        return
    
    for i in range(index,n):
        if not visited[i]:
            visited[i] = 1
            numbers.append(i+1)
            combination(numbers,i+1,count+1)
            numbers.pop()
            visited[i] = 0
            
combination([],0,0)