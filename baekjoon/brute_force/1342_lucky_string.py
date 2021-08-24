import sys
input = sys.stdin.readline

def dfs(count,last):
    global length,result
    if count == length:
        result += 1
        return
    for i in range(length):
        if not visited[i] and last != s[i]:
            visited[i] = 1
            dfs(count+1,s[i])
            visited[i] = 0

s = input().rstrip()
length = len(s)
result = 0
visited = [0] * length
dfs(0,'')
print(result)