import sys
input = sys.stdin.readline

n = int(input().rstrip())

result = 0
count = 1
for i in range(1,n+1):
    if i >= 10 ** count:
        count += 1
    result += count
        
print(result)