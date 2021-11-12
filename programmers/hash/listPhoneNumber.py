# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    pre = {}
    phone_book.sort(key=lambda x: -len(x))
    for number in phone_book:
        if number in pre.keys():
            return False
        for idx, c in enumerate(number):
            if pre[number[:idx+1]] not in pre.keys():
                pre[number[:idx+1]] = 1
    return True
