import sys
input = sys.stdin.readline

n = int(input().rstrip())
balloon = list(map(int,input().split()))
visited = [0] * n
count = 0
for i in range(n-1,-1,-1):
    if not visited[i]:
        now = balloon[i]
        visited[i] = 1
        count += 1
        for j in range(i-1,-1,-1):
            if balloon[j] == now + 1 and not visited[j]:
                now = balloon[j]
                visited[j] = 1
print(count)