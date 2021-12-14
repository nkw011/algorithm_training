# https://programmers.co.kr/learn/courses/30/lessons/87390
# 같을 때 같지 않을 때를 고려해주어야한다.

def solution(n, left, right):
    answer = []
    row_s,row_e = left // n, right // n
    col_s,col_e = (left %n), (right% n)
    if row_s != row_e:
        for num in range(col_s,n):
            if (num+1) >= (row_s+1): answer.append(num+1)
            else: answer.append(row_s+1)
        for i in range(row_s+1,row_e):
            for j in range(n):
                if i >= j: answer.append(i+1)
                else: answer.append(j+1)
        for num in range(col_e+1):
            if (num+1) >= (row_e+1): answer.append(num+1)
            else: answer.append(row_e+1)
    else:
        for num in range(col_s,col_e+1):
            if row_s >= num: answer.append(row_s+1)
            else: answer.append(num+1)
    return answer

# 참고 풀이: 그렇네.. 결국 이 한 줄로 완성이 된다...
def solution(n,left,right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer
