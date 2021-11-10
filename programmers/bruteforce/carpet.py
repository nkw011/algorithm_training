# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total = brown + yellow
    for row in range(1, int(total ** (1/2))+1):
        if total % row == 0:
            col = total // row
            if ((row * 2) + (col-2) * 2) == brown:
                return [max(row, col), min(row, col)]
