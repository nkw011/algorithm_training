import sys
input = sys.stdin.readline

def dfs(count,result):
    global possible
    if possible:
        return
    if count == n:
        temp1, temp2 = 0,0
        for a,b in clause:
            temp1 = not result[abs(a)-1] if a < 0 else result[abs(a)-1]
            temp2 = not result[abs(b)-1] if b < 0 else result[abs(b)-1]
            if not (temp1 or temp2):
                return
        possible = True
        print(1)
        for num in result:
            print(num,end=" ")
        print()
        return
    for i in range(2):
        if visited[i] < n:
            visited[i] += 1
            result.append(i)
            dfs(count+1,result)
            result.pop()
            visited[i] -= 1

n,m = map(int,input().split())
clause = []
visited = [0] * 2
possible = False
for _ in range(m):
    clause.append(tuple(map(int,input().split())))
dfs(0,[])
if not possible:
    print(0)