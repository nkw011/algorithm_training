import sys
input = sys.stdin.readline

n,m = map(int,input().split())
coins = []

for _ in range(n):
    coins.append(int(input().rstrip()))

count = 0
for i in range(n-1,-1,-1):
    count += m // coins[i]
    m %= coins[i]

print(count)