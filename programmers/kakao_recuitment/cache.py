# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    ret = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            ret += 1
        elif cacheSize != 0:
            cache.append(city)
            cacheSize -= 1
            ret += 5
        elif cache:
            cache.popleft()
            cache.append(city)
            ret += 5
        else:
            ret += 5
    return ret

# 참고 풀이: deque(maxlen)


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    ret = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            ret += 1
        else:
            cache.append(city)
            ret += 5
    return ret
