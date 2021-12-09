# https://programmers.co.kr/learn/courses/30/lessons/68645
# row,col 표시
# 6,5,4,3,2,1 방식으로 줄어듦
from functools import reduce

def solution(n):
    answer = [[0] * i for i in range(1,n+1)]
    r,c = -1,0
    number = 0
    for idx,num in enumerate(range(n,0,-1)):
        for _ in range(num):
            number += 1
            if idx % 3 == 0:
                r += 1
                answer[r][c] = number
            elif idx % 3 == 1:
                c += 1
                answer[r][c] = number
            else:
                r -= 1
                c -= 1
                answer[r][c] = number
    answer = reduce(lambda x,y: x+y,answer)
    return answer
