# https://programmers.co.kr/learn/courses/30/lessons/17679

# 1. 만족하는 것 조사하기
# 2. 없애면서 위에 있는 것 차례대로 가져오기
# 3. 다시 재조사하면서 있는지 없는지 체크해서 없으면 총 없앤 갯수 반환

loc = [(0, 0), (1, 0), (0, 1), (1, 1)]


def check_4block_condtion(i, j, m, n, board):
    for y, x in loc:
        dy = i + y
        dx = j + x
        if dy >= m or dx >= n or board[dy][dx] != board[i][j]:
            return False
    return True


def find_blocks(m, n, board):
    result = set()
    for i in range(m):
        for j in range(n):
            if board[i][j] != '' and check_4block_condtion(i, j, m, n, board):
                for y, x in loc:
                    result.add((i+y, j+x))
    return result


def solution(m, n, board):
    board = [[c for c in board[num]] for num in range(m)]
    block = list(find_blocks(m, n, board))
    cnt = 0
    while block:
        cnt += len(block)
        block.sort(key=lambda x: (x[0], x[1]))
        for y, x in block:
            if y > 0:
                for i in range(y-1, -1, -1):
                    board[i+1][x] = board[i][x]
            board[0][x] = ''
        block = list(find_blocks(m, n, board))
    return cnt
