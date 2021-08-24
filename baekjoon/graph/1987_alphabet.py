import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
alphabet = [0] * 26
visited = [[0] * c for _ in range(r)]

# 굳이 알파벳을 확인하는데 visted 연산을 사용할 필요가 없다
# 두번째로 불필요하게 ord 연산이 너무 많았다.
maxValue = 0
def dfs(i,j,count):
    global maxValue
    maxValue = max(maxValue,count)
    for x,y in move:
        dx = x + j
        dy = y + i
        if 0 <= dx < c and 0 <= dy < r :
            value = ord(matrix[dy][dx])
            if not alphabet[value - 65]:
                alphabet[value - 65] = 1
                dfs(dy,dx,count+1)
                alphabet[value - 65] = 0

alphabet[ord(matrix[0][0]) - 65] = 1
dfs(0,0,1)
print(maxValue)