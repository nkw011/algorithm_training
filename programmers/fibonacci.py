# https://programmers.co.kr/learn/courses/30/lessons/12945
# DP라서 점수를 더 많이 주는 것같다.

def solution(n):
    f = [0] * (n+1)
    f[0], f[1] = 0,1
    for i in range(2,n+1):
        f[i] = (f[i-1] + f[i-2]) % 1234567
    return f[n]
