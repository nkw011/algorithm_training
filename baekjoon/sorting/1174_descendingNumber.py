import sys
input = sys.stdin.readline

def dfs(digit, limit, numbers,last):
    global count,possible
    if digit == limit:
        count += 1
        if count == n:
            possible = True
            for number in numbers:
                print(number,end="")
            print()
        return
        
    for num in nums:
        if not visited[num] and last > num:
            visited[num] = 1
            numbers.append(num)
            dfs(digit+1,limit,numbers,num)
            visited[num] = 0
            numbers.pop()


n = int(input().rstrip())
nums = list(range(0,10))
count = 0
visited = [0] * 10
possible = False
for digit in range(1,11):
    visited = [0] * 10
    dfs(0,digit,[],10)
if not possible:
    print(-1)