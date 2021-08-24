import sys
input = sys.stdin.readline

n = int(input().rstrip())
drinks = list(map(int,input().split()))
drinks.sort(reverse=True)
result = drinks[0]
for i in range(1,n):
    result += (drinks[i] / 2)

if result - int(result) == 0:
    print(int(result))
else:
    print(result)