import sys
input = sys.stdin.readline
INF = int(1e9)

f = [0,1,1]
index = 3
while True:
    f.append(f[index-1]+f[index-2])
    if f[index] >= INF:
        break
    index += 1
    
T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    nums = []
    index = len(f)
    while n != 0:
        for i in range(index-1,-1,-1):
            if n >= f[i]:
                index = i-1
                n -= f[i]
                nums.append(f[i])
                break
    nums.sort()
    for num in nums:
        print(num,end=" ")
    print()