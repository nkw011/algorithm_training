import sys
input = sys.stdin.readline

n,m = map(int,input().split())
limits = []
miles = []
visited = [0] * n
result = 0
for i in range(n):
    now,limit = map(int,input().split())
    miles = list(map(int,input().split()))
    miles.sort(reverse=True)
    last = 1
    if limit <= now:
        last = miles[limit-1]
    limits.append(last)
limits.sort()

for lecture in limits:
    if m >= lecture:
        result += 1
        m -= lecture
print(result)