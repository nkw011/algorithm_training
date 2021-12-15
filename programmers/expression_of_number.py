# https://programmers.co.kr/learn/courses/30/lessons/12924
# 부분합은 대부분 two_pointer로 만들 수 있다.

def solution(n):
    numbers,answer = list(range(1,n+1)),0
    l,r,sums = -1,0,0
    # two-pointer인데 둘 다 끝까지 와야한다면 이렇게 활용할 수 있을 것 같다.
    # while문 2개를 가지고 구현할 수 있다.
    while l < n:
        while r < n:
            if sums < n:
                sums += numbers[r]
                r += 1
            else:
                break
        if sums == n:
            answer += 1
        if l+1 < n:
            sums -= numbers[l+1]
        l += 1
    return answer
