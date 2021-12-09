# https://programmers.co.kr/learn/courses/30/lessons/77885
# XOR: 비트가 다르면 1을 같으면 0을 반환한다.

def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = bin(num)[2:]
        for i in range(len(bin_num)):
            nxt = num+(1<<i)
            cnt = bin(num ^ nxt).count('1')
            if cnt <= 2:
                answer.append(nxt)
                break
    return answer

