# https://programmers.co.kr/learn/courses/30/lessons/17684

import re


def solution(files):
    file_sort = []
    for file in files:
        head = re.findall('\D+', file)[0]
        number = re.findall('\d+', file)[0]
        file_sort.append((head.lower(), int(number), file))
    file_sort.sort(key=lambda x: (x[0], x[1]))
    return [file[2] for file in file_sort]
