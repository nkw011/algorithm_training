# 순열이기 때문에 굳이 numSet을 이용해서 중복 체크를 할 이유가 없다
# 조합이더라도 idx를 늘리는 방식으로 해서 중복체크를 하면 될 것 같다.

import sys
input = sys.stdin.readline

def dfs(count,number):
    global result
    if count == n:
        for num in nums:
            if not visited[num]:
                return
        result += 1
        return
    for i in range(10):
        if visited[i] < n:
            visited[i] += 1
            dfs(count+1,number+(10**(n-1-count)*i))
            visited[i] -= 1

n,m = map(int,input().split())
nums = list(map(int,input().split()))
result = 0
visited = [0] * 10
dfs(0,0)
print(result)