import sys
input = sys.stdin.readline

n = int(input().rstrip())
times = []
for _ in range(n):
    start, end = map(int,input().split())
    times.append((start,end,end-start))

times.sort(key= lambda x :(x[1],x[0]))
last = -1
count = 0
for time in times :
    start, end = time[:2]
    if start >= last:
        count +=1
        last = end

print(count)