import sys
input = sys.stdin.readline

n = int(input().rstrip())
xs = []
ys = []
targets = []

for _ in range(n):
    x,y = map(int,input().split())
    xs.append(x)
    ys.append(y)
    targets.append((x,y))
xs.sort()
ys.sort()
rx,ry = 0,0
if n % 2 == 1:
    rx = xs[n//2]
    ry = ys[n//2]
else:
    rx = xs[n//2-1]
    ry = ys[n//2-1]
result = 0
for tx,ty in targets:
    result += abs(tx - rx)
    result += abs(ty - ry)
print(result)