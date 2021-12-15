# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    n,m,k = len(arr1),len(arr2),len(arr2[0])
    n_arr2 = [[0] * m for _ in range(k)]
    for i in range(m):
        for j in range(k):
            n_arr2[j][i] = arr2[i][j]
    answer = [[sum([n1 * n2 for n1,n2 in zip(a,b)]) for b in n_arr2 ]for a in arr1]
    return answer

# 참고 코드: zip(*B)가 돋보인다.

def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
