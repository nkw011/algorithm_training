# https://programmers.co.kr/learn/courses/30/lessons/12905
# 시간복잡도: O(h*w)만에 해결해야 시간초과가 나지 않는 문제였다.
# DP를 활용하여 풀었다.

def solution(board):
    n,m,answer = len(board),len(board[0]),0
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j]:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) +1
    for i in range(n):
        for j in range(m):
            if answer < board[i][j]:
                answer = board[i][j]
                
    return answer**2
