import sys
input = sys.stdin.readline

n = int(input().rstrip())
numArray = [0] *(n+1)
visited = [0] * (n+1)
result = []
count = 0
for i in range(n):
    numArray[i+1] = int(input().rstrip())
    
for i in range(1,n+1):
    if not visited[i]:
        visited[i] = 1
        if i == numArray[i]:
            result.append(i)
            count += 1
        else :
            if numArray[numArray[i]] == i:
                visited[numArray[i]] = 1
                result.append(i)
                result.append(numArray[i])
                count += 2
print(count)
result.sort()
for num in result:
    print(num)