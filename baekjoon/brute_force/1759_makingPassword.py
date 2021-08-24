import sys
input = sys.stdin.readline

l,c = map(int,input().split())
alpha = list(input().split())
alpha.sort()
visited = [0] * c
moeum = ['a','e','i','o','u']

def dfs(numbers,index,count):
    if count == l:
        count1 = 0
        for number in numbers:
            if alpha[number] in moeum:
                count1 += 1
        count2 = l- count1
        if count1 >= 1 and count2 >= 2:
            for number in numbers:
                print(alpha[number],end="")
            print()
        return
    
    for i in range(index+1,c):
        if not visited[i]:
            visited[i] = 1
            numbers.append(i)
            dfs(numbers,i,count+1)
            visited[i] = 0
            numbers.pop()
            
dfs([],-1,0)