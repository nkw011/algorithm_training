import sys
input = sys.stdin.readline

n = int(input().rstrip())
locations = [tuple(map(int,input().split())) for _ in range(n)]

locations = sorted(locations,key=lambda x:(x[1],x[0]))

for x,y in locations:
    print(x,y)