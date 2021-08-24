import sys
input = sys.stdin.readline

n = int(input().rstrip())
chains = list(map(int,input().split()))
chains.sort()
count = 0
while True:
    length = len(chains)
    if chains[0] == sum(chains):
        break
    chains[0] -= 1
    chains[length -2] += (chains[length-1] +1)
    chains.pop()
    if chains[0] == 0:
        del chains[0]
    count += 1
print(count)