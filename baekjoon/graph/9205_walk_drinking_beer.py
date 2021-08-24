# 가는 길이 계속 1000이하면 갈 수 있기 때문에 단순히 짧은 경로만을 탐색하는 것이 아닌
# 갈 수 있는 경로에 놓인 거리의 합이 최대 경로의 합보다 작은 지 살펴봐야한다.
import sys
input = sys.stdin.readline
INF = int(1e9)


T = int(input().rstrip())
for loop in range(T):
    n = int(input().rstrip())
    position = [tuple(map(int,input().split())) for _ in range(n+2)]
    matrix = [[INF] * (n+2) for _ in range(n+2)]
    
    for i in range(n+2):
        for j in range(n+2):
            number = abs(position[i][0] - position[j][0]) + abs(position[i][1] - position[j][1])
            if number <= 1000:
                matrix[i][j] = 1
            else :
                matrix[i][j] = 0

    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
                
    if matrix[0][n+1] == 1:
        print("happy")
    else :
        print("sad")

#---------------------------------------------------------------------------------

# import sys
# input = sys.stdin.readline

# INF = int(1e9)

# def visit(start):
#     global possible
#     if start == n+1:
#         possible = True
#         return

#     for i in range(n+2):
#         if i != start and not visited[i] and matrix[start][i] <= 1000:
#             visited[i] = 1
#             visit(i)
#             visited[i] = 0

# T = int(input().rstrip())
# for loop in range(T):
#     n = int(input().rstrip())
#     position = [tuple(map(int,input().split())) for _ in range(n+2)]
#     matrix = [[INF] * (n+2) for _ in range(n+2)]
    
#     for i in range(n+2):
#         for j in range(n+2):
#             number = abs(position[i][0] - position[j][0]) + abs(position[i][1] - position[j][1])
#             matrix[i][j] = number
            
#     for k in range(n+2):
#         for i in range(n+2):
#             for j in range(n+2):
#                 matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
                
#     visited = [0] * (n+2)
#     visited[0] = 1
#     possible = False
#     visit(0)
#     if possible:
#         print("happy")
#     else :
#         print("sad")


