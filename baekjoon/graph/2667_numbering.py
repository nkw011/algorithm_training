from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(map(int,input().rstrip())) for _ in range(n)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0] * n for _ in range(n)]
count = 0
nums = []
def bfs(matrix):
    global count,nums
    q = deque()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and not visited[i][j]:
                q.append((i,j))
                count += 1
                matrix[i][j] = count
                visited[i][j] = 1
                result = 1
                while q:
                    r,c = q.popleft()
                    for x,y in move:
                        dx = x + c
                        dy = y + r
                        if 0 <= dx <n and 0 <= dy < n:
                            if matrix[dy][dx] == 1 and not visited[dy][dx]:
                                visited[dy][dx] = 1
                                matrix[dy][dx] = count
                                result += 1
                                q.append((dy,dx))
                nums.append((count,result))
                
                                  
bfs(matrix)
print(count)
nums.sort(key=lambda x:x[1])
for houses in nums:
    print(houses[1])