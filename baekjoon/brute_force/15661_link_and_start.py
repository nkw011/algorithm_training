import sys
input = sys.stdin.readline

def calculate(numbers):
    value = 0
    for a in numbers:
        for b in numbers:
            value += matrix[a][b]
    return value


def dfs(numbers,index,c,count):
    global minValue
    if count == c:
        value1 = calculate(numbers)
        notNumbers = [k for k in range(n) if k not in numbers]
        value2 = calculate(notNumbers)
        minValue = min(minValue,abs(value1-value2))
        return
    
    for i in range(index+1,n):
        if not visited[i]:
            visited[i] = 1
            numbers.append(i)
            dfs(numbers,i,c,count+1)
            numbers.pop()
            visited[i] = 0


n = int(input().rstrip())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
minValue = 4000000

for num in range(1,n):
    dfs([],-1,num,0)

print(minValue)