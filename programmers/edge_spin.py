# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows,columns,queries):
    board = [[0] * columns for _ in range(rows)]
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            board[i-1][j-1] = (i-1) * columns + j
    answer = []
    for x1,y1,x2,y2 in queries:
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        temp = board[x1][y1]
        minValue = board[x1][y1]
        # left
        for i in range(x1+1,x2+1):
            board[i-1][y1] = board[i][y1]
            minValue = min(minValue,board[i][y1])
        
        for j in range(y1+1,y2+1):
            board[x2][j-1] = board[x2][j]
            minValue = min(minValue,board[x2][j])
        
        for i in range(x2-1,x1-1,-1):
            board[i+1][y2] = board[i][y2]
            minValue = min(minValue,board[i][y2])
        
        for j in range(y2-1,y1,-1):
            board[x1][j+1] = board[x1][j]
            minValue = min(minValue,board[x1][j])
        board[x1][y1+1] = temp
        answer.append(minValue)
    return answer
