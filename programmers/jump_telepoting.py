# https://programmers.co.kr/learn/courses/30/lessons/12980

# 풀이 방법
# 1. 2로 나누어 떨어지지않을 때까지 n을 2로 계속 나눠준다.
# 2. n이 0보다 크면 1을 뺀 이후 1번, 아니면 종료

# 첫번째 풀이: while문을 사용하였으나 구조가 조금 이상함
def solution(n):
    cnt = 0
    while n > 0:
        while n % 2 == 0:
            n //= 2
        if n > 0:
            cnt += 1
            n -= 1
    return cnt

# # 두번째 풀이: recursive function을 활용
def solution(n):
    if n == 0: return 0
    if n%2: return 1+solution(n-1)
    else: return solution(n//2)

# 세번째 풀이: 첫번째 풀이를 개선한 풀이 어차피 두번째 while문을 지나면 무조건 0보다 크기 때문에(제일 작은 수가 1임) if n >0을 없앰
def solution(n):
    cnt = 0
    while n > 0:
        while n % 2 == 0:
            n //= 2
        cnt += 1
        n -= 1
    return cnt
