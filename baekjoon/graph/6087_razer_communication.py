# 반례 모음집 : https://bingorithm.tistory.com/2

# razer가 닿는 모든 곳에서 하면 좋을 것 갇다.
# 이걸 어떻게 다시 바꿀까.. 크흠...
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start,d):
    global minCount
    visited = [[0] * w for _ in range(h)]
    visited[razer[0][0]][razer[0][1]] = 1
    visited[start[0]][start[1]] = 1
    q = deque()
    q.append((start[0],start[1],d,0))
    while q:
        i,j, direc,count = q.popleft()
        for index in range(4):
            dx = j + mx[index]
            dy = i + my[index]
            if 0 <= dy < h and 0 <= dx < w:
                if not visited[dy][dx]:
                    if (dy,dx) == razer[1]:
                        result = count if (index//2) == direc else count +1
                        minCount = min(minCount,result)
                        return
                    elif matrix[dy][dx] == '.':
                        visited[dy][dx]= 1
                        if direc != (index//2):
                            q.append((dy,dx,index//2,count+1))
                            continue
                        q.append((dy,dx,index//2,count))
    return -1

w,h = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(h)]
razer = []
for i in range(h):
    for j in range(w):
        if matrix[i][j] == 'C':
            razer.append((i,j))
minCount = w * h +1
mx = [1,-1,0,0]
my = [0,0,1,-1]

# 가로 먼저
for j in range(razer[0][1],w):
    if matrix[razer[0][0]][j] != '*':
        bfs((razer[0][0],j),0)
    else :
        break
for j in range(razer[0][1],-1,-1):
    if matrix[razer[0][0]][j] != '*':
        bfs((razer[0][0],j),0)
    else :
        break

for i in range(razer[0][0],h):
    if matrix[i][razer[0][1]] != '*':
        bfs((i,razer[0][1]),1)
    else :
        break
for i in range(razer[0][0],-1,-1):
    if matrix[i][razer[0][1]] != '*':
        bfs((i,razer[0][1]),1)
    else :
        break
print(minCount)


# import sys
# input = sys.stdin.readline
# from collections import deque
# import heapq

# def bfs():
#     visited[razer[0][0]][razer[0][1]] = 1
#     q = []
#     heapq.heappush(q,(razer[0][0],razer[0][1],0,0))
#     first = True
#     while q:
#         i,j, direc, count = heapq.heappop(q)
#         for index in range(4):
#             dx = j + mx[index]
#             dy = i + my[index]
#             if 0<= dy < h and 0 <= dx < w:
#                 if not visited[dy][dx]:
#                     if matrix[dy][dx] == 'C':
#                         return count if direc == index // 2 else count+1
#                     elif matrix[dy][dx] == '.': 
#                         if first:
#                             visited[dy][dx] = 1
#                             q.append((dy,dx,index//2,0))
#                         else :
#                             visited[dy][dx] = 1
#                             if direc != (index//2):
#                                 q.append((dy,dx,index//2,count+1))
#                                 continue
#                             q.append((dy,dx,direc,count))
#             if index == 3:
#                 first = False
#     return -1


# w,h = map(int,input().split())
# matrix = [list(input().rstrip()) for _ in range(h)]
# razer = []
# for i in range(h):
#     for j in range(w):
#         if matrix[i][j] =='C':
#             razer.append((i,j))
# visited = [[0] * w for _ in range(h)]
# mx = [1,-1,0,0]
# my = [0,0,1,-1]

# print(bfs())

##################################### 두번째 방법 ##########################################

# from collections import deque
# import heapq

# def bfs():
#     visited[razer[0][0]][razer[0][1]]= [1,1]
#     q = []
#     heapq.heappush(q,(0,razer[0][0],razer[0][1],0))
#     first = True
#     while q:
#         count,i,j, direc = heapq.heappop(q)
#         for index in range(4):
#             dx = j + mx[index]
#             dy = i + my[index]
#             if 0<= dy < h and 0 <= dx < w:
#                 if not visited[dy][dx][index//2]:
#                     if matrix[dy][dx] == 'C':
#                         return count if direc == index // 2 else count+1
#                     elif matrix[dy][dx] == '.':  
#                         if first:
#                             visited[dy][dx][index//2] = 1
#                             heapq.heappush(q,((0,dy,dx,index//2)))
#                         else :
#                             visited[dy][dx][index//2] = 1
#                             if direc != (index//2):
#                                 heapq.heappush(q,(count+1,dy,dx,index//2))
#                                 continue
#                             heapq.heappush(q,(count,dy,dx,direc))
#             if index == 3:
#                 first = False
#     return -1


# w,h = map(int,input().split())
# matrix = [list(input().rstrip()) for _ in range(h)]
# razer = []
# for i in range(h):
#     for j in range(w):
#         if matrix[i][j] =='C':
#             razer.append((i,j))
# visited = [[[0,0] for _ in range(w)] for _ in range(h)]
# mx = [1,-1,0,0]
# my = [0,0,1,-1]

# print(bfs())