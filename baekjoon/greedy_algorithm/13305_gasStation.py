import sys
input = sys.stdin.readline

n = int(input().rstrip())
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

cost = costs[0]
total = 0
for i in range(n-1):
    if cost > costs[i]:
        cost = costs[i]
    total += (cost * roads[i])
print(total)