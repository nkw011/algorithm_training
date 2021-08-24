import sys
input = sys.stdin.readline

n = int(input().rstrip())
trees = list(map(int,input().split()))
degree = list(map(int,input().split()))
length = [ (degree[i],trees[i])for i in range(n)]
length.sort()
result = 0
count = 0
for leng in length:
    result += (leng[0] * count + leng[1])
    count +=1
print(result)