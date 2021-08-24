import sys
input = sys.stdin.readline

n, a, d  = map(int,input().split())
eums = list(map(int,input().split()))

count = 0
nxt = a
for eum in eums:
    if eum == nxt:
        nxt += d
        count += 1
print(count)